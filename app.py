from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"id": "1", "nome": "Mauro", "email": "mauro@gmail.com", "perfil": "Coordenador", "status": "Ativo"},
    {"id": "2", "nome": "Giovanna", "email": "giovanna@gmail.com", "perfil": "Aluno", "status": "Ativo"},
    {"id": "3", "nome": "Gabriel", "email": "gabriel@gmail.com", "perfil": "Aluno", "status": "Ativo"},
    {"id": "4", "nome": "Miguel", "email": "miguel@gmail.com", "perfil": "Aluno", "status": "Inativo"},
    {"id": "5", "nome": "Vinicius", "email": "vinicius@gmail.com", "perfil": "Professor", "status": "Ativo"},
    {"id": "6", "nome": "Zayra", "email": "zayra@gmail.com", "perfil": "Aluno", "status": "Ativo"},
    {"id": "7", "nome": "Diógenes", "email": "diogenes@gmail.com", "perfil": "Professor", "status": "Inativo"}
]

@app.route("/user/<nome>")
def user_page(nome):
    return render_template("user.html", nome=nome)
 
@app.route("/users")
def list_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
