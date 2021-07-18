from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from datos import db
class Vendedor(db.Model):
    __tablename__ = 'Vendedor'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(40), nullable=False)
    fecha_ingreso = Column(Date(), nullable=False)
    activo = Column(Boolean(True), nullable=False)
    # ???
    # direccion = Column(String(40), nullable=False)
    # dni = Column(String(40), nullable=False)
