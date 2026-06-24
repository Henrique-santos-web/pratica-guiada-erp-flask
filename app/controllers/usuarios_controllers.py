from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import Usuario

def listar_todos_usuarios():
    return Usuario.query.order_by(Usuario.id.desc()).all()


def obter_usuario(usuario_id): #* O parametro pega dados através da URL
    return Usuario.query.get_or_404(usuario_id) #* passamos os dados pra cá e é feito uma verificação 
    #* Vai em Usuario, faz uma consulta(query), se estiver no Usuario o id recebido, ok, se não, erro 404


def salvar_usuario(nome, email, senha=None, usuario_id=None): #* a senha e usuario_id é none, pois hora de editar, eu posso acabar editando apenas o nome e email, mas não a senha
                                                              #* sobre o usuario_id, é none, pois na criação de um usuário, como vou passar um ID se um usuário nem existe ainda? 
                                                              #* por padrão, caso não seja preenchido os campos de senha ou usuario, ele recebe None
    if not nome or not email:
        return False, "Nome e Email são campos obrigatórios."

    try:
        if usuario_id: #* MODO DE EDIÇÃO DO USUÁRIO
            usuario = obter_usuario(usuario_id)
            usuario.nome = nome
            usuario.email = email

            if senha and senha.strip():
                usuario.set_senha(senha)

            mensagem = "Usuario atualizado com sucesso!"

        else: #* MODO DE CADASTRO DO USUÁRIO
            if not senha:
                return False, "A senha é obrigatória para novos usuários."

            usuario = Usuario(nome=nome, email=email)
            usuario.set_senha(senha)
            db.session.add(usuario)
            mensagem = "Usuario cadastrado com sucesso!"

        db.session.commit()
        return True, mensagem

    except IntegrityError: #* Aqui deduz que o erro seja no email, mas esse "IntegrityError" verifica qualquer erro que possa acontecer no banco de dados
        db.session.rollback()
        return False, "Erro: Este e-mail já está cadastrado."


    except Exception as e:
        db.session.rollback()
        return False, f"Erro interno: {str(e)}"


def excluir_usuario(usuario_id):
    usuario = obter_usuario(usuario_id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        return True, "Usuario excluído com sucesso!"
    except Exception as e:
        db.session.rollback()
        return False, f"Erro ao excluir usuário: {str(e)}"