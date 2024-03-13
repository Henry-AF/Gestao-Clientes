from flask import Flask, render_template
from routes.home import home_route
from routes.clientes import cliente_route

#inicialização
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

#Execução
app.run(debug=True)