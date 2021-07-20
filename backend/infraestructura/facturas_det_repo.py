from dominio.detalles import Detalle
from datos import db

# facturas, no se modifican ni se eliminan

class FacturasDetalleRepo():
    def get_all(self):
        return Detalle.query.all()
    

    def agregar(self, data):
        a = Detalle(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return Detalle.query.get(id)

## total general buscando todos los detalles que haya en x factura 
# 
# 
# aunque deberiamos hacer en el front
    def calcular_total(self, id):
        total = 0.00
        d= Detalle.query.get(id)
        for x in d:
            total +=(x.articulo_cantidad * x.articulo_precio)
            return total

