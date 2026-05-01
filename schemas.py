from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    categoria: str
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: str | None = None
    preco: float | None = None
    categoria: str | None = None
    quantidade: int | None = None

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True