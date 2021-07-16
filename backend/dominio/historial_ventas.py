from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from backend.datos import db
class Historial_Ventas(db.Model):
    # codigo - descripcion - cantidad vendida - monto total (con iva)
    __tablename__ = 'historial_ventas'
    #Relacion con Articulo/Producto?
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(40), nullable=False)
    cantidad = Column(Integer(), nullable=False)
    total = Column(Float(),True)
