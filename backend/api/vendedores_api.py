from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.vendedores_repo import VendedoresRepo

from flask_restx.inputs import date

repo = VendedoresRepo()

nsVendedor = Namespace('vendedores', description='Administrador de vendedores')

modeloVendedorSinID = Model('VendedorSinCod',{
    'nombre': fields.String(),
    'fecha_ingreso': fields.Date(),
    'activo': fields.Boolean()
})

modeloVendedor = modeloVendedorSinID.clone('Vendedor',{
    'codigo': fields.Integer(),
})

nsVendedor.models[modeloVendedor.name] = modeloVendedor
nsVendedor.models[modeloVendedorSinID.name] = modeloVendedorSinID

nuevoVendedorParser = reqparse.RequestParser(bundle_errors=True)
nuevoVendedorParser.add_argument('nombre', type=str, required=True)
nuevoVendedorParser.add_argument('fecha_ingreso', type=str, required=True)
nuevoVendedorParser.add_argument('activo', type=bool, required=False, default=True)

editarVendedorParser = nuevoVendedorParser.copy()
editarVendedorParser.add_argument('codigo',type=int, required=True)

@nsVendedor.route('/')
class VendedorResource(Resource):
    @nsVendedor.marshal_list_with(modeloVendedor)
    def get(self):
        ## traigo los que tan en stock nomas
        return repo.get_activos()

    @nsVendedor.expect(modeloVendedorSinID)
    @nsVendedor.marshal_with(modeloVendedor)
    def post(self):
        data = nuevoVendedorParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsVendedor.route('/<int:id>')
class VendedorResource(Resource):
    @nsVendedor.marshal_with(modeloVendedor)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    @nsVendedor.expect(modeloVendedor)
    def put(self, id):
        data = editarVendedorParser.parse_args()
        if repo.modificar(id,data):
            return 'Vendedor actualizado', 200
        abort(404)
   

@nsVendedor.route('/baja/<int:id>')
class VendedorResource(Resource):
    @nsVendedor.expect(modeloVendedor)

    def put(self, id):
        if repo.baja(id):
            repo.baja(id)
                       
            return 'Vendedor dado de Baja', 200            
        abort(400)
        