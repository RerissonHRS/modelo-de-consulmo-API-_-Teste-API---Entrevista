README - Projeto 1 (CRUD básico em memória)
# API de Usuários - CRUD Simples (FastAPI)

Este projeto é uma API simples criada para praticar chamadas HTTP usando Postman.  
Ele implementa um CRUD básico de usuários utilizando apenas memória (sem banco de dados).

## Tecnologias
- Python
- FastAPI
- Uvicorn

## Instalação

Clone o repositório e instale as dependências:

```bash
pip install fastapi uvicorn

Executando o Servidor
uvicorn main:app --reload


A API ficará disponível em:

http://127.0.0.1:8000


Documentação interativa (Swagger):

http://127.0.0.1:8000/docs

Rotas para Testar no Postman
Método	Rota	Descrição
GET	/	Testa se a API está ativa
POST	/usuarios?nome=NOME&idade=IDADE	Cria um usuário
GET	/usuarios	Lista todos os usuários
GET	/usuarios/{id}	Busca um usuário pelo ID
PUT	/usuarios/{id}?nome=NOME&idade=IDADE	Atualiza um usuário
DELETE	/usuarios/{id}	Remove um usuário
Exemplo de Criação de Usuário no Postman
POST http://127.0.0.1:8000/usuarios?nome=Joao&idade=25


Retorno esperado:

{
  "id": 1,
  "nome": "Joao",
  "idade": 25
}
