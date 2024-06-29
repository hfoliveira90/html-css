from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/quemsomos")
def quem():
    return render_template("quemsomos.html")


@app.route("/contatos")
def contato():
    return render_template("contatos.html")
