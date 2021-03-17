from flask import render_template,request,redirect,url_for,flash
from app import init_app
from app.migrate import init_db



app = init_app()

@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html',error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('error/500.html',error=error)

@app.route('/database')
def database():
    init_db()
    return 'base de datos creada'

if __name__ == '__main__':
    app.run(debug = True)