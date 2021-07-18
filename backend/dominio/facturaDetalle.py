# cantidad, codigo de producto, descripcion de producto, precio unitario, porcentaje de iva aplicado (21 o
# 10.5), subtotal.
from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from backend.datos import db
class FacturaDetalle(db.Model):
    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'facturas_detalle'
    #Relacion con Articulo/Producto?
    
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    articulo = relationship
    cantidad = Column(Integer(), nullable=False)
    total = Column(Float(),nullable=False)
