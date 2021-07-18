from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from datos import db
class Vendedor(db.Model):
    __tablename__ = 'tipos_factura'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(1), nullable=False)
    iva = Column(Float(), nullable=False)
