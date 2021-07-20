# Factura de venta: fecha, nro de factura, letra, vendedor, datos del cliente (nombre, dir,
# tel, cuit, localidad), detalle de lo vendido con precios, total general. Opcional: nro de
# presupuesto.
# from sqlalchemy import Integer, ForeignKey, String, Column, Float
# from sqlalchemy.orm import relationship
# from datos import db
# from sqlalchemy.types import Date
# class FacturaVenta(db.Model):

#     # codigo - descripcion - cantidad vendida - monto total (con iva)
#     __tablename__ = 'facturas_venta'
#     #Relacion con Articulo/Producto?
#     numero = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     tipo = Column(String)
#     vendedor = relationship('Vendedor')
#     vendedor_id= Column(Integer,  ForeignKey('Vendedor.codigo'))   
#     cliente_id =Column(Integer, ForeignKey('cliente.codigo'))
#     cliente =relationship("Cliente", back_populates="factura_venta")
#     detalle =  relationship("VentaDetalle", backref="factura_venta")
#     total = Column(Float())
#     fecha = Column(Date())
