from flask import Flask, render_template


app = Flask("Olá mundo")

@app.route("/alunos")
def alunos():
    return render_template("hello.html")
