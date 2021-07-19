from dominio.facturaDetalle import FacturaDetalle
from datos import db

# facturas, no se modifican ni se eliminan

class FacturasDetalleRepo():
    def get_all(self):
        return FacturaDetalle.query.all()
    

    def agregar(self, data):
        a = FacturaDetalle(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return FacturaDetalle.query.get(id)
