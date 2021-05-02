from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Usuario(UserMixin,db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    name =db.Column(db.String(80),nullable=False)
    username =db.Column(db.String(80),nullable=False,)
    password =db.Column(db.String(250),nullable=False,)
    is_admin =db.Column(db.Boolean,default=False)
    avatar =db.Column(db.String(250),default=False)
     
    def __repr__(self):
        return 'USERNAME:{}, EMAIL:{}'.format(self.username,self.email)
    
    #para encriptar la clave
    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)   
    
class Categoria(db.Model):
   
    id=db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(40))
    
class Producto(db.Model):
    
    id=db.Column(db.Integer,primary_key= True)
    nombre = db.Column(db.String(80))
    precio = db.Column(db.String(15))
    peso = db.Column(db.String(15))
    categoria_id = db.Column(db.Integer(),db.ForeignKey('categoria.id',ondelete ='CASCADE'))
    categoria = db.relationship('Categoria', backref = db.backref('productos',lazy=True))
    
