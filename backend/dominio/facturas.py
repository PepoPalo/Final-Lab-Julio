# Factura de compra: fecha, nro de factura, letra, datos del proveedor (nombre, dir, tel,
# cuit, localidad), detalle de lo comprado con precios, total general.
from sqlalchemy.types import Date
from sqlalchemy import Integer, ForeignKey, String, Column, Float
from sqlalchemy.orm import relationship
from datos import db


class Factura(db.Model):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    total = Column(Float())
    tipo = Column(String)


class Venta(Factura):

    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_venta'
    #Relacion con Articulo/Producto?
    numero = Column(Integer, unique=True)
    vendedor_id= Column(Integer, ForeignKey('Vendedor.codigo'))   
    cliente_id =Column(Integer, ForeignKey('cliente.codigo'))
    detalle =  relationship("VentaDetalle", backref="factura_venta",lazy='joined')
    total = Column(Float())
    fecha = Column(Date())


class Compra(Factura):

    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_compra'
    #Relacion con Articulo/Producto?
    numero = Column(Integer)
    proveedor_cod = Column(Integer, ForeignKey('proveedores.codigo'), nullable=True) 
    detalle =  relationship("CompraDetalle", backref="factura_compra",lazy='joined')


class Presupuesto(Factura):
    __tablename__ = 'presupesto'

    fecha_ingreso = Column(Date)
    fecha_validez = Column(Date)
    vendedor_id= Column(Integer, ForeignKey('Vendedor.codigo'))   
    cliente_id =Column(Integer, ForeignKey('cliente.codigo'))
    detalle = relationship("PresupuestoDetalle", backref="presupuesto",lazy='joined')
