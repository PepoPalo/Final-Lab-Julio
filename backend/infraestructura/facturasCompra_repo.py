from dominio.facturas import Compra
from datos import db

# facturas, no se modifican ni se eliminan

class FacturasCompraRepo():
    def get_all(self):
        return Compra.query.all()
    

    def agregar(self, data):
        a = Compra(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return Compra.query.get(id)

