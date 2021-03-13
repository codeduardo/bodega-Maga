from database import db

class Categoria(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(40))
    
class Producto(db.Model):
    id=db.Column(db.Integer,primary_key= True)
    nombre = db.Column(db.String(80))
    precio = db.Column(db.String(15))
    peso = db.Column(db.String(15))
    categoria_id = db.Column(db.Integer(),db.ForeignKey('categoria.id'))
    categoria = db.relationship('Categoria', backref = db.backref('productos',lazy=True))
        