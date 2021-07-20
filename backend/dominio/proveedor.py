from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datos import db

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(40), nullable=False)
    direccion = Column(String(80), nullable=False)
    telefono = Column(String(40),nullable=False)
    cuit = Column(String(40), nullable=False)
    localidad = Column(String(40), nullable=False)
    factura_compra = relationship("FacturaCompra", backref="proveedor")
