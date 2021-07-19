# Factura de venta: fecha, nro de factura, letra, vendedor, datos del cliente (nombre, dir,
# tel, cuit, localidad), detalle de lo vendido con precios, total general. Opcional: nro de
# presupuesto.
from sqlalchemy import Integer, ForeignKey, String, Column, Float
from sqlalchemy.orm import relationship
from datos import db
from sqlalchemy.types import Date
class FacturaVenta(db.Model):

    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_venta'
    #Relacion con Articulo/Producto?
    ### CORREGIR AUTOINCREMENT
    numero = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    # tipo_id =relationship('TipoFactura', foreign_keys='Factura.tipo.codigo')
    # tipo =relationship('TipoFactura', backref='FacturaVenta', foreign_keys='FacturaVenta.tipo_id')
    vendedor = relationship('Vendedor')
    vendedor_id= Column(Integer, foreign_keys='Vendedor.codigo')   
    cliente_id =relationship('Cliente', foreign_keys='cliente.cuit')
    cliente =relationship('Cliente', backref='FacturaVenta')
    detalle =  relationship('FacturaDetalle',foreign_keys='FacturaVenta.numero', backref='FacturaVenta')
    total = Column(Float())
    fecha = Column(Date())


