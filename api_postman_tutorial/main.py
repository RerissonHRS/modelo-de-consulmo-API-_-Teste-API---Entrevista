from fastapi import FastAPI, HTTPException

app = FastAPI()

# Banco de dados em memória (simples)
usuarios = []

@app.get("/")
def home():
    return {"mensagem": "API funcionando! Teste rotas no Postman."}

@app.post("/usuarios")
def criar_usuario(nome: str, idade: int):
    novo_usuario = {"id": len(usuarios) + 1, "nome": nome, "idade": idade}
    usuarios.append(novo_usuario)
    return novo_usuario

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{id_usuario}")
def buscar_usuario(id_usuario: int):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.put("/usuarios/{id_usuario}")
def atualizar_usuario(id_usuario: int, nome: str, idade: int):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["nome"] = nome
            usuario["idade"] = idade
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{id_usuario}")
def deletar_usuario(id_usuario: int):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
