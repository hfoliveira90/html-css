from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask("__name__")
todos_email = []
#CONECTANDO FLASK AO DATABASE
mysql = MySQL(app)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'perfectblue2015'
app.config['MYSQL_DB'] = 'emails'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/roteiros")
def roteiros():
    return render_template('roteiros.html')


@app.route("/contato", methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        #RECEBENDO INFORMAÇÕES DO FORMULÁRIO
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        telefone = request.form['telefone']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        #gravar informações no banco de dados
        with app.app_context():
            #ABRE A CONEXÃO COM DB
            cursor = mysql.connection.cursor()

            #INSERE AS INFORMAÇÕES NUM COMANDO SQL
            cursor.execute('''insert into email (nome, sobrenome, telefone, email, assunto, mensagem) VALUES (%s, %s, %s, %s, %s, %s)''', (nome, sobrenome, telefone, email, assunto, mensagem))
            mysql.connection.commit()

            #FECHA A CONEXÃO
            cursor.close()
            return redirect(url_for('lista'))
    return render_template('contato.html')

@app.route("/lista")
def lista():
        #ABRE A CONEXÃO COM DB
        cursor = mysql.connection.cursor()

        #INSERE AS INFORMAÇÕES NUM COMANDO SQL
        cursor.execute('''SELECT * FROM email ''')
        mysql.connection.commit()
        todos_email = cursor.fetchall()

        #FECHA A CONEXÃO
        cursor.close()
        return render_template('lista.html', todos_email = todos_email)

