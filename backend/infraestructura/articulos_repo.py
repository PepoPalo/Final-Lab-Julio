from backend.dominio.articulo import Articulo
from backend.datos import db


class ArticulosRepo():
    def get_all(self):
        return Articulo.query.all()
    
    def get_enStock(self):
        return Articulo.query.filter(Articulo.enStock == True).all()


    def agregar(self, data):
        a = Articulo(**data)
        db.session.add(a)
        db.session.commit()
        return a
    
    def get_by_id(self, id):
        return Articulo.query.get(id)

    def baja(self,id):
        a = Articulo.query.get(id)
        if a:
            db.session.delete(a)
            a.enStock = False
            db.session.commit()
            return True
        return False

    def modificar(self, id, data):
        a = Articulo.query.get(id)
        if a:
            a.codigo = data['codigo']
            a.descripcion = data.get('descripcion', None)
            a.precio = data['precio']
            a.enStock = data['enStock']
            return True
        return False