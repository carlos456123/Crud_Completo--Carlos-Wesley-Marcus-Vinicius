# CRUD com FastAPI

##  Integrantes

* Carlos Wesley
* Marcus Vinicius

---

##  Instalação e Execução

Instale as dependências:

```
pip install fastapi uvicorn sqlalchemy
```

Execute a API:

```
uvicorn main:app --reload
```

Acesse a documentação interativa no navegador:

```
http://127.0.0.1:8000/docs
```

---

## Estrutura do Projeto

O projeto foi organizado em módulos para melhor organização e manutenção:

* `main.py` → rotas da API
* `models.py` → definição das tabelas (banco de dados)
* `schemas.py` → validação dos dados (entrada e saída)
* `crud.py` → lógica das operações (CRUD)
* `database.py` → conexão com o banco SQLite

---

## ⚙️ Decisões Técnicas

### 📌 Banco de Dados

Foi utilizado o **SQLite**, conforme exigido na atividade, garantindo persistência dos dados.

---

### 📌 Estrutura

Optamos por dividir o projeto em múltiplos arquivos (modularização), facilitando:

* organização do código
* manutenção futura
* melhor entendimento da aplicação

---

### 📌 Status Codes

Foram utilizados os seguintes códigos HTTP:

* **201** → criação de produto
* **200** → operações bem-sucedidas
* **204** → deleção de produto
* **404** → produto não encontrado

---

### 📌 Campos

* No **POST**: todos os campos são obrigatórios, garantindo integridade dos dados
* No **PATCH**: os campos são opcionais, permitindo atualização parcial

---

### 📌 Respostas

Todas as rotas retornam dados no formato **JSON**, conforme padrão de APIs REST.

---

##  Funcionalidades da API

A API permite:

* Listar todos os produtos
* Buscar um produto por ID
* Criar um novo produto
* Atualizar um produto (completo ou parcial)
* Deletar um produto

---

##  Observação

O projeto foi desenvolvido com base no conteúdo estudado em aula.
