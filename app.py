from flask import Flask, render_template

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app = Flask("Olá mundo")

@app.route("/")
def alunos():
    return render_template("hello.html")
