from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "faculdade"

@app.route("/")
def lista():
    cursor = mysql.get_db().cursor()
    return render_template("listarprofessores.html", professor = get_professores(cursor))

@app.route('/consultarportitulacao', methods=['GET', 'POST'])
def titulo():
    if request.method == 'POST':
        titulo = request.form.get('titulo')

        cursor = mysql.get_db().cursor()

        titulacao = get_titulo(cursor, titulo)

        if titulacao is None:
            return render_template("listarprofessor.html", erro='Se não há exigência, pode escolher qualquer professor a baixo.')
        else:
            cursor = mysql.get_db().cursor()
            return render_template("consultarportitulacao.html", tituloprof = get_titulo(cursor, titulo))

    else:
        return render_template('listarprofessor.html', erro='Método errado, Use Post')



@app.route('/exibirprofessor/<professores>')
def detalhes(professores):
    cursor = mysql.get_db().cursor()
    return render_template("exibirprofessores.html", detalhes = get_detalhes(cursor, professores))


@app.route('/calcularsalarioprofessor/<detalhe>')
def salario(detalhe):
    y = int(detalhe)
    x = (50 * y)
    return render_template("calcularsalarioprofessor.html", salario = x)

if __name__ == '__main__':
    app.run(debug=True)