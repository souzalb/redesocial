from flask import render_template, url_for, redirect, session
from rede import app, database, bcrypt
from rede.models import User, Photo
from flask_login import login_required, login_user, logout_user, current_user
from rede.forms import LoginForm, RegisterForm, PhotoForm
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def homepage():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user and bcrypt.check_password_hash(user.password, loginform.password.data):
            login_user(user)
            return redirect(url_for("feed", user_id=user.id))
    return render_template("homepage.html", form=loginform)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        password = bcrypt.generate_password_hash(registerform.password.data)
        user = User(username=registerform.username.data, password=password, email=registerform.email.data)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("perfil", user_id=user.id))
    return render_template("criarconta.html", form=registerform)

@app.route("/perfil/<user_id>", methods=["GET", "POST"])
@login_required
def perfil(user_id):
    if int(user_id) == int(current_user.id):
        #o usuário visualiza o próprio perfil
        photo_form = PhotoForm()
        if photo_form.validate_on_submit():
            file = photo_form.photo.data
            secure_name = secure_filename(file.filename)
            #salva o arquivo na pasta posts_photos
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_name)
            file.save(path)
            #registrar o arquivo no banco de dados
            photo = Photo(file_name=secure_name, user_id=current_user.id)
            database.session.add(photo)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=photo_form)
    else:
        user = User.query.get(int(user_id))
        return render_template("perfil.html", usuario=user, form=None)

@app.route("/feed")
@login_required
def feed():
    photos = Photo.query.order_by(Photo.upload_date.desc()).all()
    return render_template("feed.html", photos=photos)