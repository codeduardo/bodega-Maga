from flask import render_template,flash,request,redirect,url_for
from flask_login import login_required


from . import category
from ..database import Categoria, db
from ..forms import CategoriaForm

@category.route('/')
@login_required
def home():
    categorias = Categoria.query.all()
    num_categorias = Categoria.query.count()
    
    return render_template('category/homeC.html',categorias = categorias,cantidad = num_categorias)

@category.route('/create', methods = ['GET','POST'])
def create():
    
    categoria = Categoria()
    categoriaForm= CategoriaForm(obj=categoria)
    if request.method =='POST':
        if categoriaForm.validate_on_submit():
            categoriaForm.populate_obj(categoria)
            
            db.session.add(categoria)
            db.session.commit()
            flash('categoria creada',category='success')
            
            return redirect(url_for('category.home'))
    
    return render_template('category/createC.html',categoriaForm=categoriaForm)

@category.route('/update/<int:id>', methods = ['GET','POST'])
def update(id) :
    categoria = Categoria.query.get_or_404(id)
    categoriaForm= CategoriaForm(obj=categoria)
    if request.method == 'POST':
        if categoriaForm.validate_on_submit():
            categoriaForm.populate_obj(categoria)
            
            
            db.session.commit()
            flash('categoria actualizada',category='success')
            return redirect(url_for('category.home'))
    return render_template('category/updateC.html',categoriaForm=categoriaForm)

@category.route('/delete/<int:id>')
def delete(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    
    db.session.commit()
    
    flash('categoria eliminada',category='success')
    return redirect(url_for('category.home'))