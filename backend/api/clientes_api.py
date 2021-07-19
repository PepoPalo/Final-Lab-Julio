from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.clientes_repo import ClientesRepo

repo = ClientesRepo()



nsCliente = Namespace('Clientes', description='Administrador de Clientes')

modeloClienteSinID = Model('ClienteSinCod',{
    'nombre': fields.String(),
    'direccion': fields.String(),
    'telefono': fields.String(),
    'cuit': fields.String(),
    'localidad': fields.String(),
    'activo': fields.Boolean(),


})

modeloCliente = modeloClienteSinID.clone('Cliente',{
    'codigo': fields.Integer()

})
# modeloBusqueda = Model('BusquedaFechas', {
#     'desde': fields.Date(),
#     'hasta': fields.Date()
# })

nsCliente.models[modeloCliente.name] = modeloCliente
nsCliente.models[modeloClienteSinID.name] = modeloClienteSinID
# nsCliente.models[modeloBusqueda.name] = modeloBusqueda

nuevoClienteParser = reqparse.RequestParser(bundle_errors=True)
nuevoClienteParser.add_argument('nombre', type=str, required=True)

nuevoClienteParser.add_argument('direccion', type=str, required=True)
nuevoClienteParser.add_argument('telefono', type=str, required=True)
nuevoClienteParser.add_argument('cuit', type=str, required=True)
nuevoClienteParser.add_argument('localidad', type=str, required=True)

nuevoClienteParser.add_argument('activo', type=bool, required=False, default=True)

editarClienteParser = nuevoClienteParser.copy()
editarClienteParser.add_argument('codigo',type=int, required=True)



@nsCliente.route('/')
class ClienteResource(Resource):
    @nsCliente.marshal_list_with(modeloCliente)
    def get(self):
        ## traigo los que tan en stock nomas
        return repo.get_all()

    @nsCliente.expect(modeloClienteSinID)
    @nsCliente.marshal_with(modeloCliente)
    def post(self):
        data = nuevoClienteParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsCliente.route('/<int:id>')
class ClienteResource(Resource):
    @nsCliente.marshal_with(modeloCliente)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    @nsCliente.expect(modeloCliente)
    def put(self, id):
        data = editarClienteParser.parse_args()
        if repo.modificar(id,data):
            return 'Cliente actualizado', 200
        abort(404)
   

# @nsCliente.route('/buscar/<string:desde>/<string:hasta>/')
# class ClienteResource(Resource):
#     @nsCliente.marshal_list_with(modeloCliente)
#     def get(self, desde, hasta):
#         l = repo.buscar(desde, hasta)
#         if l:
#             return l, 200
#         abort(404)


# @nsCliente.route('/baja/<int:id>')
# class ClienteResource(Resource):
#     @nsCliente.expect(modeloCliente)

#     def put(self, id):
#         if repo.baja(id):
#             repo.baja(id)
                       
#             return 'Cliente dado de Baja', 200            
#         abort(400)
        