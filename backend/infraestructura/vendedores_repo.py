from dominio.vendedor import Vendedor
from datos import db


class VendedoresRepo():
    def get_all(self):
        return Vendedor.query.all()
    
    def get_activos(self):
        return Vendedor.query.filter(Vendedor.activo == True).all()

    def agregar(self, data):
        v = Vendedor(**data)
        
        db.session.add(v)
        db.session.commit()
        return v
    
    def get_by_id(self, id):
        return Vendedor.query.get(id)

    def baja(self,id):
        v = Vendedor.query.get(id)
        if v:
            v.activo = False
            return True
        return False

    def modificar(self, id, data):
        v = Vendedor.query.get(id)
        if v:
            v.codigo = data['codigo']
            v.nombre = data.get['nombre']
            v.fecha_ingreso = data['fecha_ingreso']
            v.activo = data['activo']
            return True
        return False