from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from backend.datos import db
class Articulo(db.Model):
    __tablename__ = 'articulos'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(20), nullable=False)
    precio = Column(Float(), nullable=False)
    enStock = Column(Boolean(),True)