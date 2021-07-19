from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.facturas_det_repo import FacturasDetalleRepo

from flask_restx.inputs import date

repo = FacturasDetalleRepo()



nsFacturaDetalle = Namespace('FacturasDetalle', description='Administrador de detalles de factura')

modeloFacturaDetalleSinID = Model('FacturaDetalleSinCod',{
    'factura_id': fields.Integer(),
    'articulo_cod': fields.Integer(),
    'articulo_cantidad': fields.Integer(),
    'articulo_precio': fields.Float(),
    'articulo_con_iva': fields.Float()
})

modeloFacturaDetalle = modeloFacturaDetalleSinID.clone('FacturaDetalle',{
    'codigo': fields.Integer(),

})
# modeloBusqueda = Model('BusquedaFechas', {
#     'desde': fields.Date(),
#     'hasta': fields.Date()
# })

nsFacturaDetalle.models[modeloFacturaDetalle.name] = modeloFacturaDetalle
nsFacturaDetalle.models[modeloFacturaDetalleSinID.name] = modeloFacturaDetalleSinID
# nsFacturaDetalle.models[modeloBusqueda.name] = modeloBusqueda

nuevoFacturaDetalleParser = reqparse.RequestParser(bundle_errors=True)
nuevoFacturaDetalleParser.add_argument('factura_id', type=int, required=True)
nuevoFacturaDetalleParser.add_argument('articulo_cod', type=int, required=True)
nuevoFacturaDetalleParser.add_argument('articulo_cantidad', type=int, required=True)
nuevoFacturaDetalleParser.add_argument('articulo_precio', type=float, required=True)
nuevoFacturaDetalleParser.add_argument('articulo_con_iva', type=float, required=True)

editarFacturaDetalleParser = nuevoFacturaDetalleParser.copy()
editarFacturaDetalleParser.add_argument('codigo',type=int, required=True)



@nsFacturaDetalle.route('/')
class FacturaDetalleResource(Resource):
    @nsFacturaDetalle.marshal_list_with(modeloFacturaDetalle)
    def get(self):
        ## traigo los que tan en stock nomas
        return repo.get_all()

    @nsFacturaDetalle.expect(modeloFacturaDetalleSinID)
    @nsFacturaDetalle.marshal_with(modeloFacturaDetalle)
    def post(self):
        data = nuevoFacturaDetalleParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsFacturaDetalle.route('/<int:id>')
class FacturaDetalleResource(Resource):
    @nsFacturaDetalle.marshal_with(modeloFacturaDetalle)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    @nsFacturaDetalle.expect(modeloFacturaDetalle)
    def put(self, id):
        data = editarFacturaDetalleParser.parse_args()
        if repo.modificar(id,data):
            return 'Detalle actualizado', 200
        abort(404)
   

# @nsFacturaDetalle.route('/buscar/<string:desde>/<string:hasta>/')
# class FacturaDetalleResource(Resource):
#     @nsFacturaDetalle.marshal_list_with(modeloFacturaDetalle)
#     def get(self, desde, hasta):
#         l = repo.buscar(desde, hasta)
#         if l:
#             return l, 200
#         abort(404)


# @nsFacturaDetalle.route('/baja/<int:id>')
# class FacturaDetalleResource(Resource):
#     @nsFacturaDetalle.expect(modeloFacturaDetalle)

#     def put(self, id):
#         if repo.baja(id):
#             repo.baja(id)
                       
#             return 'Detalle dado de Baja', 200            
#         abort(400)
        