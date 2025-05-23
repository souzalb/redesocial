from flask import render_template, url_for
from rede import app
from flask_login import login_required
from rede.forms import LoginForm, RegisterForm

@app.route("/", methods=["GET", "POST"])
def homepage():
    loginform = LoginForm()
    return render_template("homepage.html", form=loginform)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    registerform = RegisterForm()
    return render_template("criarconta.html", form=registerform)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)



