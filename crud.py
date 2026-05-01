from models import Produto

def listar_produtos(db):
    return db.query(Produto).all()

def buscar_produto(db, produto_id):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def criar_produto(db, produto):
    novo = Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_produto(db, produto_id, dados):
    produto = buscar_produto(db, produto_id)
    if produto:
        for key, value in dados.dict(exclude_unset=True).items():
            setattr(produto, key, value)
        db.commit()
        db.refresh(produto)
    return produto

def substituir_produto(db, produto_id, dados):
    produto = buscar_produto(db, produto_id)
    if produto:
        produto.id = dados.id
        produto.nome = dados.nome
        produto.preco = dados.preco
        produto.categoria = dados.categoria
        produto.quantidade = dados.quantidade
        db.commit()
        db.refresh(produto)
    return produto

def deletar_produto(db, produto_id):
    produto = buscar_produto(db, produto_id)
    if produto:
        db.delete(produto)
        db.commit()
    return produto