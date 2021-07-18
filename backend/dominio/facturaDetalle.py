# cantidad, codigo de producto, descripcion de producto, precio unitario, porcentaje de iva aplicado (21 o
# 10.5), subtotal.
from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from backend.datos import db
from sqlalchemy.sql.schema import ForeignKey
class FacturaDetalle(db.Model):
    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_detalle'
    #Relacion con Articulo/Producto?
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    factura_id = Column(Integer, unique=False)
    articulo_cod = Column(String(), nullable=False)
    articulo_cantidad = Column(Integer(), nullable=False)
    articulo_precio = Column(Float(), nullable=False)
    articulo_con_iva = Column(Float(), nullable=False)


    # VER RELACIONAR CON HISTORIAL


    
    # factura = Column(ForeignKey('factura.codigo'))
   # factura_id =relationship("Factura", foreign_keys='Factura.codigo', backref='FacturaDetalle')
    # factura = relationship("Factura", foreign_keys='FacturaDetalle.factura_id', backref='FacturaDetalle')
   ## iva_aplicado = relationship('TipoFactura', backref='FacturaDetalle')
    # iva_aplicado = relationship('Factura',foreign_keys='Factura.tipo.iva', backref='FacturaDetalle')

    # iva_aplicado= Column(Float(),nullable=False)
    # total = Column(Float(),nullable=False)
