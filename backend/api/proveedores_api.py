from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.proveedores_repo import ProveedoresRepo

repo = ProveedoresRepo()

nsProveedor = Namespace('Proveedores', description='Administrador de Proveedores')

modeloProveedorSinID = Model('ProveedoreSinCod',{
    'nombre': fields.String(),
    'direccion': fields.String(),
    'telefono': fields.String(),
    'cuit': fields.String(),
    'localidad': fields.String(),
    'activo': fields.Boolean(),
})

modeloProveedor = modeloProveedorSinID.clone('Proveedor',{
    'codigo': fields.Integer()

})

nsProveedor.models[modeloProveedor.name] = modeloProveedor
nsProveedor.models[modeloProveedorSinID.name] = modeloProveedorSinID

nuevoProveedoreParser = reqparse.RequestParser(bundle_errors=True)
nuevoProveedoreParser.add_argument('nombre', type=str, required=True)
nuevoProveedoreParser.add_argument('direccion', type=str, required=True)
nuevoProveedoreParser.add_argument('telefono', type=str, required=True)
nuevoProveedoreParser.add_argument('cuit', type=str, required=True)
nuevoProveedoreParser.add_argument('localidad', type=str, required=True)
nuevoProveedoreParser.add_argument('activo', type=bool, required=False, default=True)

editarProveedoreParser = nuevoProveedoreParser.copy()
editarProveedoreParser.add_argument('codigo',type=int, required=True)



@nsProveedor.route('/')
class ProveedoreResource(Resource):
    @nsProveedor.marshal_list_with(modeloProveedor)
    def get(self):
        ## traigo los que tan en stock nomas
        return repo.get_all()

    @nsProveedor.expect(modeloProveedorSinID)
    @nsProveedor.marshal_with(modeloProveedor)
    def post(self):
        data = nuevoProveedoreParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsProveedor.route('/<int:id>')
class ProveedoreResource(Resource):
    @nsProveedor.marshal_with(modeloProveedor)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    @nsProveedor.expect(modeloProveedor)
    def put(self, id):
        data = editarProveedoreParser.parse_args()
        if repo.modificar(id,data):
            return 'Proveedor actualizado', 200
        abort(404)
   
