from flask import Flask, render_template

#Objeto/servidor do Flask
app = Flask(__name__)

#rota principal
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    mensagem = None

    if request.method == 'POST':
        Email = request.form.get('email')
        Nome = request.form.get('username')
        Senha = request.form.get('senha')
        mensagem = f"Cadastro concluído para {nome} com o email {email} efetuado com sucesso."

    return render_template('formulario.html', mensagem=mensagem)