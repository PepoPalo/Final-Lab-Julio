from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from datos import db
from api.articulos_api import nsArticulo
from api.vendedores_api import nsVendedor
from api.clientes_api import nsCliente
from api.facturas_det_api import nsFacturaDetalle
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:100letters@localhost/Facturacion"

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()


api = Api(app, version='1.0.beta', title='Telefonía', description='Administracion de servicio de Facturacion')

api.add_namespace(nsArticulo)
api.add_namespace(nsVendedor)
api.add_namespace(nsCliente)
api.add_namespace(nsFacturaDetalle)



if __name__ == '__main__':
    app.run()