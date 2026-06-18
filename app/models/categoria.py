from app.extensions import db

class Categoria(db.Model): #* o class Categoria(db.Model) diz que Categoria é filha da Model (pra saber mais, apenas lendo a documentação)
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)

    produtos = db.relationship("Produto", backref="categoria", lazy=True) #* esse lazy carrega as info de forma mais lenta
    #* vai até categoria, procura produto e armazena na variavel produtos

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }