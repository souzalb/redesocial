from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    return 'Rede Social de Fotos - Tela Inicial'

@app.route("/perfil")
def perfil():
    return 'Rede Social de Fotos - Perfil'

if __name__ == '__main__':
    app.run(debug=True)
