from dominio.cliente import Cliente
from datos import db


class ClientesRepo():
    def get_all(self):
        return Cliente.query.all()
    
 
    def agregar(self, data):
        c = Cliente(**data)
        db.session.add(c)
        db.session.commit()
        return c
    
    def get_by_id(self, id):
        return Cliente.query.get(id)

    def baja(self,id):
        c = Cliente.query.get(id)
        if c:
            c.activo = False
            return True
        return False

    def modificar(self, id, data):
        c = Cliente.query.get(id)
        if c:
            c.codigo = data['codigo']
            c.nombre = data.get['nombre']
            c.direccion = data['direccion']
            c.telefono = data['telefono']
            c.cuit = data['cuit'] 
            c.localidad = data['localidad']
            c.activo = data['activo']
            return True
        return False