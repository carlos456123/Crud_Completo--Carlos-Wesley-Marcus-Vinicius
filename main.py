from fastapi import FastAPI, HTTPException
from database import SessionLocal
import crud, schemas

app = FastAPI()

def get_db():
    return SessionLocal()

@app.get("/produtos", response_model=list[schemas.ProdutoResponse])
def listar():
    db = get_db()
    return crud.listar_produtos(db)

@app.get("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def buscar(produto_id: int):
    db = get_db()
    produto = crud.buscar_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos", response_model=schemas.ProdutoResponse, status_code=201)
def criar(produto: schemas.ProdutoCreate):
    db = get_db()
    return crud.criar_produto(db, produto)

@app.put("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def substituir(produto_id: int, dados: schemas.ProdutoCreate):
    db = get_db()
    produto = crud.substituir_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.patch("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def atualizar(produto_id: int, dados: schemas.ProdutoUpdate):
    db = get_db()
    produto = crud.atualizar_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.delete("/produtos/{produto_id}")
def deletar(produto_id: int):
    db = get_db()
    produto = crud.deletar_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"mensagem": "Produto deletado"}