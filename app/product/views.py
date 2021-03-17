from flask import render_template,request, redirect, url_for


from . import product
from ..database import Categoria, Producto, db
from ..forms import CategoriaForm, ProductoForm

@product.route('/view/<int:id>', methods = ['GET','POST'])   
def home(id):
    categoria = Categoria.query.get_or_404(id)
    productos = Producto.query.filter(Producto.categoria_id == id).all()
    return render_template('product/homeP.html', categoria = categoria, productos=productos)
 

@product.route('/create/<int:id>',methods = ['GET','POST'])
def create(id):
    categoria = Categoria.query.get_or_404(id)
    producto = Producto()
    productoForm = ProductoForm(obj = producto)
    if request.method =='POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('category.home'))
    return render_template('product/createP.html',productoForm=productoForm,categoria = categoria)
    
    


@product.route('/update/<int:id>',methods = ['GET','POST'])
def update(id):
    producto = Producto.query.get_or_404(id)
    productoForm = ProductoForm(obj=producto)
    if request.method == 'POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            db.session.commit()
            return redirect(url_for('category.home'))
    return render_template('product/updateP.html',productoForm=productoForm)



@product.route('/delete/<int:id>')
def delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('category.home'))