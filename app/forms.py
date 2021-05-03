from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,PasswordField
from wtforms.validators import DataRequired,Length

class CategoriaForm(FlaskForm):
    nombre =StringField('Nombre',validators=[DataRequired()])
    enviar =SubmitField('Guardar')
    
class ProductoForm(FlaskForm):
    nombre=StringField('Nombre',validators=[DataRequired()])
    precio=StringField('Precio',validators=[DataRequired()])
    peso=StringField('Peso( ml,l,gr )',validators=[DataRequired()])
    categoria_id = IntegerField('Categoria_id',validators=[DataRequired()])
    guardar = SubmitField('Guardar')
    
class LoginForm(FlaskForm):
    username = StringField('Username:',validators = [DataRequired()])
    password = PasswordField('Password:', validators = [DataRequired()])
    login = SubmitField('LOGIN') 

class searchForm(FlaskForm):
    courseName = StringField('Busca Producto', validators=[DataRequired(), Length(max=60)])