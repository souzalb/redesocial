from flask import render_template, url_for, redirect
from rede import app, database, bcrypt
from rede.models import User, Photo
from flask_login import login_required, login_user, logout_user, current_user
from rede.forms import LoginForm, RegisterForm

@app.route("/", methods=["GET", "POST"])
def homepage():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user and bcrypt.check_password_hash(user.password, loginform.password.data):
            login_user(user)
            return redirect(url_for("perfil", user_id=user.id))
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

@app.route("/perfil/<user_id>")
@login_required
def perfil(user_id):
    if int(user_id) == int(current_user.id):
        #o usuário visualiza o próprio perfil
        return render_template("perfil.html", usuario=current_user)
    else:
        user = User.query.get(int(user_id))
        return render_template("perfil.html", usuario=user)





