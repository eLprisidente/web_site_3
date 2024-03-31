from flask import Flask, render_template, redirect, request
from data import db_session
from data.forms.LoginForm import LoginForm
from data.forms.add_jobs import JobForm
from data.forms.add_comment import CommentForm
from data.forms.user import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import tempfile

from data.jobs import Jobs
from data.users import User
from data.comments import Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init("db/mars.db")


@app.route('/')
def index():
    db_sess = db_session.create_session()
    context = {}
    context["jobs"] = db_sess.query(Jobs).all()
    context["comments"] = db_sess.query(Comment).all()
    return render_template('index.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    add_form = JobForm()
    print(add_form.picture.data)
    if add_form.validate_on_submit():
        filename = add_form.picture.data.filename
        file_object = add_form.picture.data.stream

        db_sess = db_session.create_session()
        jobs = Jobs(
            post=add_form.post.data,
            author=current_user.name,
            description=add_form.description.data,
            picture=filename,
            photo=file_object.read()
        )
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Добавить пост',
                           form=add_form)


@app.route('/add_comment',  methods=['GET', 'POST'])
@login_required
def add_comment():
    add_form = CommentForm()
    if add_form.validate_on_submit():
        db_sess = db_session.create_session()
        comments = Comment(
            comment=add_form.comment.data,
            author=current_user.name,
            post_id=add_form.post_id.data
        )
        db_sess.add(comments)
        db_sess.commit()
        return redirect('/')
    return render_template('add_comment.html', title='Добавить комментарий',
                           form=add_form)


@app.route('/post_del/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()

    return redirect('/')


@app.route('/post_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = JobForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if jobs:
            jobs.post = form.post.data
            jobs.description = form.description.data
            jobs.picture = form.picture.data
            db_sess.commit()
            return redirect('/')

    return render_template('edit_job.html',
                           title='Редактирование поста',
                           form=form
                           )


if __name__ == '__main__':
    app.run(port=8098, host='127.0.0.1')
