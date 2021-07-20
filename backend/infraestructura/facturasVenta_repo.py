from dominio.facturas import Venta
from datos import db

# facturas, no se modifican ni se eliminan

class FacturasVentaRepo():
    def get_all(self):
        return Venta.query.all()
    

    def agregar(self, data):
        a = Venta(**data)
        a.numero = len(Venta.query.all())+1
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return Venta.query.get(id)

