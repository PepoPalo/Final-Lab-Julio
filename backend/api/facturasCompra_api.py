from flask import abort
from flask_restx import Resource, Namespace, Model, fields, reqparse
from infraestructura.facturasCompra_repo import FacturasCompraRepo
from infraestructura.vendedores_repo import VendedoresRepo
from flask_restx.inputs import date
# from dominio.vendedor import Vendedor
# from dominio.cliente import Cliente
#from dominio.facturaDetalle import FacturaDetalle
from .clientes_api import modeloCliente
from .proveedores_api import modeloVendedor


repo = FacturasCompraRepo()


nsFacturaCompra = Namespace('FacturasCompra', description='Administrador de facturas de compra')

modeloFacturaCompraSinID = Model('FacturaCompraSinID',{
    'tipo': fields.String(),
    'proveedor_id': fields.Integer(),
    'total': fields.Float(),
    'fecha': fields.Date()
    # ?????????????????
})

modeloFacturaCompra = modeloFacturaCompraSinID.clone('FacturaCompra',{
    'numero': fields.Integer(),
    'proveedor': fields.Nested(modeloProveedor, skip_none=True)
})
# modeloBusqueda = Model('BusquedaFechas', {
#     'desde': fields.Date(),
#     'hasta': fields.Date()
# })

nsFacturaCompra.models[modeloFacturaCompra.name] = modeloFacturaCompra
nsFacturaCompra.models[modeloFacturaCompraSinID.name] = modeloFacturaCompraSinID
# nsFacturaCompra.models[modeloBusqueda.name] = modeloBusqueda

nuevoFacturaCompraParser = reqparse.RequestParser(bundle_errors=True)
nuevoFacturaCompraParser.add_argument('tipo', type=str, required=True)
nuevoFacturaCompraParser.add_argument('vendedor_id', type=int, required=True)
nuevoFacturaCompraParser.add_argument('cliente_id', type=int, required=True)

# # # ver como declaramos objetos vendedor, cliente, tipo(factura), detalle
################################################################################
#nuevoFacturaCompraParser.add_argument('cliente', required=True)
#nuevoFacturaCompraParser.add_argument('vendedor', required=True)
#nuevoFacturaCompraParser.add_argument('detalle',  required=True)
################################################################################
# nuevoFacturaCompraParser.add_argument('tipo',  required=True)


nuevoFacturaCompraParser.add_argument('total', type=float, required=True)
nuevoFacturaCompraParser.add_argument('fecha', type=date, required=True)


@nsFacturaCompra.route('/')
class FacturaCompraResource(Resource):
    @nsFacturaCompra.marshal_list_with(modeloFacturaCompra)
    def get(self):
        return repo.get_all()

    @nsFacturaCompra.expect(modeloFacturaCompraSinID)
    @nsFacturaCompra.marshal_with(modeloFacturaCompra)
    def post(self):
        data = nuevoFacturaCompraParser.parse_args()
        p = repo.agregar(data)
        if p:
            return p, 200
        abort(500)

@nsFacturaCompra.route('/<int:id>')
class FacturaCompraResource(Resource):
    @nsFacturaCompra.marshal_with(modeloFacturaCompra)
    def get(self, id):
        p = repo.get_by_id(id)
        if p:
            return p, 200
        abort(404)
    
    
    
    # @nsFacturaCompra.expect(modeloFacturaCompra)
    # def put(self, id):
    #     data = editarFacturaCompraParser.parse_args()
    #     if repo.modificar(id,data):
    #         return 'Factura de Compra actualizada', 200
    #     abort(404)
   

# @nsFacturaCompra.route('/buscar/<string:desde>/<string:hasta>/')
# class FacturaCompraResource(Resource):
#     @nsFacturaCompra.marshal_list_with(modeloFacturaCompra)
#     def get(self, desde, hasta):
#         l = repo.buscar(desde, hasta)
#         if l:
#             return l, 200
#         abort(404)


# @nsFacturaCompra.route('/baja/<int:id>')
# class FacturaCompraResource(Resource):
#     @nsFacturaCompra.expect(modeloFacturaCompra)

#     def put(self, id):
#         if repo.baja(id):
#             repo.baja(id)
                       
#             return 'Detalle dado de Baja', 200            
#         abort(400)
        