from app.extensions import db
from app.models import Categoria, Produto

def listar_todas_categorias():
    return Produto.query.order_by(Produto.id.desc()).all()


def obter_categoria(categoria_id):
    return Categoria.query.get_or_404(categoria_id)