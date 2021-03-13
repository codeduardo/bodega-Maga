from flask import Flask,render_template,request,redirect,url_for
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from database import db
from models import Categoria,Producto
from forms import CategoriaForm,ProductoForm


app = Flask(__name__)
Bootstrap(app)

USER='postgres'
PASS='admin'
HOST='localhost'
NAME_DB='TIENDA1'
FULL_URL_DB = f'postgresql://{USER}:{PASS}@{HOST}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
  
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)
# ejecutar en la terminal flask db init
# luego ejecutar en la terminal flask db migrate
# luego ejecutar en la terminal flask db upgrade

# si se quiere modificar hacerlo siguiente
# ejecutar en la terminal flask db stamp head
# luego ejecutar en la terminal flask db migrate
# luego ejecutar en la terminal flask db upgrade


# configuracion flask-wtf
app.config['SECRET_KEY'] = 'llave_secreta'


@app.route('/')
def inicio():
    categorias = Categoria.query.all()
    num_categorias = Categoria.query.count()
    
    return render_template('index.html',categorias = categorias,cantidad = num_categorias)

@app.route('/ver/<int:id>', methods = ['GET','POST'])   
def ver(id):
    categoria = Categoria.query.get_or_404(id)
    productos = Producto.query.filter(Producto.categoria_id == id).all()
    return render_template('productoindex.html', categoria = categoria, productos=productos)
 
@app.route('/agregar', methods = ['GET','POST'])
def agregar():
    categoria = Categoria()
    categoriaForm= CategoriaForm(obj=categoria)
    if request.method =='POST':
        if categoriaForm.validate_on_submit():
            categoriaForm.populate_obj(categoria)
            
            db.session.add(categoria)
            db.session.commit()
            return redirect(url_for('inicio'))
    
    return render_template('agregar.html',categoriaForm=categoriaForm)
@app.route('/agregarP/<int:id>',methods = ['GET','POST'])
def agregarP(id):
    categoria = Categoria.query.get_or_404(id)
    producto = Producto()
    productoForm = ProductoForm(obj = producto)
    if request.method =='POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarP.html',productoForm=productoForm,categoria = categoria)
    
    
@app.route('/editar/<int:id>', methods = ['GET','POST'])
def actualizar(id) :
    categoria = Categoria.query.get_or_404(id)
    categoriaForm= CategoriaForm(obj=categoria)
    if request.method == 'POST':
        if categoriaForm.validate_on_submit():
            categoriaForm.populate_obj(categoria)
            
            db.session.commit()
            
            return redirect(url_for('inicio'))
    return render_template('actualizar.html',categoriaForm=categoriaForm)

@app.route('/actualizar/producto/<int:id>',methods = ['GET','POST'])
def actualizarP(id):
    producto = Producto.query.get_or_404(id)
    productoForm = ProductoForm(obj=producto)
    if request.method == 'POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('actualizarP.html',productoForm=productoForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminar/producto/<int:id>')
def eliminarP(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug = True)