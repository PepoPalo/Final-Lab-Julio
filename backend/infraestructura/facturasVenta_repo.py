from dominio.facturaVenta import FacturaVenta
from datos import db

# facturas, no se modifican ni se eliminan

class FacturasVentaRepo():
    def get_all(self):
        return FacturaVenta.query.all()
    

    def agregar(self, data):
        a = FacturaVenta(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return FacturaVenta.query.get(id)

