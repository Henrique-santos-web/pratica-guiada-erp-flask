from app.extensions import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)
    #* db.ForeignKey("categorias.id")
    #* db.ForeignKey = passando o comando de fazer uma ligação com algumja tabela
    #* ("categorias.id") = vai até categoria e procura o id que na qual terá essa relação


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "categoria": self.categoria.nome
        }