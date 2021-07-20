# cantidad, codigo de producto, descripcion de producto, precio unitario, porcentaje de iva aplicado (21 o
# 10.5), subtotal.
from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from datos import db
from sqlalchemy.sql.schema import ForeignKey


class Detalle(db.Model):
    __abstract__ = True
    
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    articulo_cod = Column(String(), nullable=False)
    articulo_cantidad = Column(Integer(), nullable=False)
    articulo_precio = Column(Float(), nullable=False)
    articulo_con_iva = Column(Float(), nullable=False)


class VentaDetalle(Detalle):
    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_detalle'
    factura_id = Column(Integer, ForeignKey('facturas_venta.numero'))
    fecha = Column(Date)


class CompraDetalle(Detalle):
    __tablename__ = 'compra_detalle'
    factura_id = Column(Integer, ForeignKey('facturas_compra.numero'))


class PresupuestoDetalle(Detalle):
    __tablename__ = 'presupuesto_detalle'
    presupuesto_id = Column(Integer, ForeignKey('facturas_venta.numero'), unique=False)
