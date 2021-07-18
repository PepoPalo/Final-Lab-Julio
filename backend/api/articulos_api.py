from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.articulos_repo import ArticulosRepo

from flask_restx.inputs import date

repo = ArticulosRepo()



nsArticulo = Namespace('articulos', description='Administrador de articulos')

modeloArticuloSinID = Model('ArticuloSinCod',{
    'descripcion': fields.String(),
    'precio': fields.String(),
    'enStock': fields.Boolean()
})

modeloArticulo = modeloArticuloSinID.clone('Articulo',{
    'codigo': fields.Integer(),

})
# modeloBusqueda = Model('BusquedaFechas', {
#     'desde': fields.Date(),
#     'hasta': fields.Date()
# })

nsArticulo.models[modeloArticulo.name] = modeloArticulo
nsArticulo.models[modeloArticuloSinID.name] = modeloArticuloSinID
# nsArticulo.models[modeloBusqueda.name] = modeloBusqueda

nuevoArticuloParser = reqparse.RequestParser(bundle_errors=True)
nuevoArticuloParser.add_argument('descripcion', type=str, required=True)
nuevoArticuloParser.add_argument('precio', type=str, required=True)
nuevoArticuloParser.add_argument('enStock', type=bool, required=False, default=True)

editarArticuloParser = nuevoArticuloParser.copy()
editarArticuloParser.add_argument('codigo',type=int, required=True)


# buscarArticulosParser = reqparse.RequestParser(bundle_errors=True)
# buscarArticulosParser.add_argument('desde', type=str, required=True)
# buscarArticulosParser.add_argument('hasta', type=str, required=True)
@nsArticulo.route('/')
class ArticuloResource(Resource):
    @nsArticulo.marshal_list_with(modeloArticulo)
    def get(self):
        ## traigo los que tan en stock nomas
        return repo.get_enStock()

    @nsArticulo.expect(modeloArticuloSinID)
    @nsArticulo.marshal_with(modeloArticulo)
    def post(self):
        data = nuevoArticuloParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsArticulo.route('/<int:id>')
class ArticuloResource(Resource):
    @nsArticulo.marshal_with(modeloArticulo)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    @nsArticulo.expect(modeloArticulo)
    def put(self, id):
        data = editarArticuloParser.parse_args()
        if repo.modificar(id,data):
            return 'Articulo actualizado', 200
        abort(404)
   

# @nsArticulo.route('/buscar/<string:desde>/<string:hasta>/')
# class ArticuloResource(Resource):
#     @nsArticulo.marshal_list_with(modeloArticulo)
#     def get(self, desde, hasta):
#         l = repo.buscar(desde, hasta)
#         if l:
#             return l, 200
#         abort(404)


@nsArticulo.route('/baja/<int:id>')
class ArticuloResource(Resource):
    @nsArticulo.expect(modeloArticulo)

    def put(self, id):
        if repo.baja(id):
            repo.baja(id)
                       
            return 'Articulo dado de Baja', 200            
        abort(400)
        