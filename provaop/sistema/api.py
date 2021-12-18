from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from controladores.controlador_producao import Controladorproducao

app = Flask(__name__)
run_with_ngrok(app)

controladorproducao = Controladorproducao()

@app.route("/producao", methods=["POST"])
def cadastrar_producao():
    try:
        dados = request.get_json()
        cod = dados["cod"]
        descricao = dados["descricao"]
        preco = dados["preco"]
        controladorproducao.cadastrar_producao(
                    cod,
                    descricao,
                    preco,
                )
        return {"status": "OK", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}

@app.route("/producao/<cod>", methods=["PUT"])
def atualizar_producao(cod):
    try:
        dados = request.get_json()
        cod = dados["cod"]
        descricao = dados["descricao"]
        preco = dados["preco"]
        controladorproducao.cadastrar_producao(
                    cod,
                    descricao,
                    preco,
                )
        return {"status": "OK", "mensagem": "Atualizado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao atualizar"}

@app.route("/producao/<cod>", methods=["DELETE"])
def excluir_producao(cod):
    try:
        controladorproducao.excluir_producao(cod)
        return {"status": "OK", "mensagem": "Excluído com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao excluir"}


@app.route("/login", methods=["POST"])
def verificar_usuario_senha():
    try:
        dados = request.get_json()
        usuario = dados["usuario"]
        senha = dados["senha"]
        if controladorUsuario.verificar_usuario_senha(usuario, senha):
            return {"status": "OK", "mensagem": "Acesso OK!"}
        else:
            return {"status": "ERRO", "mensagem": "Usuário/Senha Inválidos!"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao efetuar o login"}

@app.route("/producao", methods=["GET"])
def listar_todos_producoes():
    try:
        todos = controladorproducao.buscar_todos_producoes()
        return jsonify(todos)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter a lista de produções"}

@app.route("/producao/<cod>")
def listar_producao(cod):
    try:
        producao = controladorproducao.buscar_producao_por_cod(cod)
        if producao:
            return jsonify(producao)
        else:
            return {"status": "ERRO", "mensagem": f"Erro ao obter a produção referida {cod}"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter a produção referida"}

if __name__ == "__main__":
    app.run(debug=True)
