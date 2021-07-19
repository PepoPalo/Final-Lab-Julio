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
            c.enStock = False
            return True
        return False

    def modificar(self, id, data):
        c = Cliente.query.get(id)
        if c:
            c.codigo = data['codigo']
            c.descripcion = data.get('descripcion', None)
            c.precio = data['precio']
            c.enStock = data['enStock']
            return True
        return False