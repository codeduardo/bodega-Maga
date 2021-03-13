from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class CategoriaForm(FlaskForm):
    nombre =StringField('Nombre',validators=[DataRequired()])
    enviar =SubmitField('Guardar')
    
class ProductoForm(FlaskForm):
    nombre=StringField('Nombre',validators=[DataRequired()])
    precio=StringField('Precio',validators=[DataRequired()])
    peso=StringField('Peso( ml,l,gr )',validators=[DataRequired()])
    categoria_id = IntegerField('Categoria_id',validators=[DataRequired()])
    guardar = SubmitField('Guardar')
    