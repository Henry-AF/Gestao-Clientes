from flask import Blueprint, render_template,request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
    -- Rotas de clientes --

    - /clientes/ (GET) - Listar clientes
    - /clientes/ (POST) - Inserir os dados do cliente
    - /clientes/new (GET) - Renderizar um formulário para criar um cliente
    - /clientes/<id> (GET) - Obter os dados de um cliente
    - /clientes/<id>/edit (GET) - Renderizar um formulário para editar um cliente
    - /clientes/<id>/update (PUT) - Atualizar os dados de um cliente
    - /clientes/<id>/delete (DELETE) - Deleta os dados de um cliente
    

"""
@cliente_route.route('/')
def lista_cliente():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    
    data = request.json
    
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    }
    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
     return render_template("form_cliente.html")

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template("detalhe_cliente.html") 

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template("form_edit_cliente.html") 

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass 

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass 