from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.facturasVenta_repo import FacturasVentaRepo
from infraestructura.vendedores_repo import VendedoresRepo
from flask_restx.inputs import date
from dominio.vendedor import Vendedor
from dominio.cliente import Cliente
from dominio.facturaDetalle import FacturaDetalle


repo = FacturasVentaRepo()
repoVendedor = VendedoresRepo()


nsFacturaVenta = Namespace('FacturasVenta', description='Administrador de facturas de venta')

modeloFacturaVentaSinID = Model('FacturaVentaSinID',{
    # 'tipo_id': fields.Integer(),
    'vendedor_id': fields.Integer(),
    'cliente_id': fields.Integer(),
    'cliente': Cliente,
    'vendedor': Vendedor,    
    'detalle': fields.List(FacturaDetalle),
    'total': fields.Float(),
    'fecha': fields.Date()
    # ?????????????????
    
})

modeloFacturaVenta = modeloFacturaVentaSinID.clone('FacturaVenta',{
    'numero': fields.Integer(),

})
# modeloBusqueda = Model('BusquedaFechas', {
#     'desde': fields.Date(),
#     'hasta': fields.Date()
# })

nsFacturaVenta.models[modeloFacturaVenta.name] = modeloFacturaVenta
nsFacturaVenta.models[modeloFacturaVentaSinID.name] = modeloFacturaVentaSinID
# nsFacturaVenta.models[modeloBusqueda.name] = modeloBusqueda

nuevoFacturaVentaParser = reqparse.RequestParser(bundle_errors=True)
nuevoFacturaVentaParser.add_argument('tipo_id', type=int, required=True)
nuevoFacturaVentaParser.add_argument('vendedor_id', type=int, required=True)
nuevoFacturaVentaParser.add_argument('cliente_id', type=int, required=True)

# # # ver como declaramos objetos vendedor, cliente, tipo(factura), detalle
################################################################################
nuevoFacturaVentaParser.add_argument('cliente', required=True)
nuevoFacturaVentaParser.add_argument('vendedor', required=True)
nuevoFacturaVentaParser.add_argument('detalle',  required=True)
################################################################################
# nuevoFacturaVentaParser.add_argument('tipo',  required=True)


nuevoFacturaVentaParser.add_argument('total', type=float, required=True)
nuevoFacturaVentaParser.add_argument('fecha', type=date, required=True)


@nsFacturaVenta.route('/')
class FacturaVentaResource(Resource):
    @nsFacturaVenta.marshal_list_with(modeloFacturaVenta)
    def get(self):
        return repo.get_all()

    @nsFacturaVenta.expect(modeloFacturaVentaSinID)
    @nsFacturaVenta.marshal_with(modeloFacturaVenta)
    def post(self):
        data = nuevoFacturaVentaParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsFacturaVenta.route('/<int:id>')
class FacturaVentaResource(Resource):
    @nsFacturaVenta.marshal_with(modeloFacturaVenta)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    # @nsFacturaVenta.expect(modeloFacturaVenta)
    # def put(self, id):
    #     data = editarFacturaVentaParser.parse_args()
    #     if repo.modificar(id,data):
    #         return 'Factura de Venta actualizada', 200
    #     abort(404)
   

# @nsFacturaVenta.route('/buscar/<string:desde>/<string:hasta>/')
# class FacturaVentaResource(Resource):
#     @nsFacturaVenta.marshal_list_with(modeloFacturaVenta)
#     def get(self, desde, hasta):
#         l = repo.buscar(desde, hasta)
#         if l:
#             return l, 200
#         abort(404)


# @nsFacturaVenta.route('/baja/<int:id>')
# class FacturaVentaResource(Resource):
#     @nsFacturaVenta.expect(modeloFacturaVenta)

#     def put(self, id):
#         if repo.baja(id):
#             repo.baja(id)
                       
#             return 'Detalle dado de Baja', 200            
#         abort(400)
        