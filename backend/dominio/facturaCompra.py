# Factura de compra: fecha, nro de factura, letra, datos del proveedor (nombre, dir, tel,
# cuit, localidad), detalle de lo comprado con precios, total general.

from sqlalchemy import Integer, ForeignKey, String, Column, Float
from sqlalchemy.orm import relationship
class FacturaCompra(db.Model):

    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_compra'
    #Relacion con Articulo/Producto?
    numero = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    tipo_id =relationship('TipoFactura', foreign_keys='Factura.tipo.codigo')
    tipo =relationship('TipoFactura', backref='FacturaCompra', foreign_keys='FacturaCompra.tipo_id')
    proveedor = relationship('Proveedor', backref='FacturaCompra')   
    detalle =  relationship('FacturaDetalle',foreign_keys='FacturaCompra.numero', backref='FacturaCompra')
    total = Column(Float(),True)



