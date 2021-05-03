from .database import *
def create_db():
    db.drop_all()
    db.create_all()
def init_db():    
    create_db()
    admin = Usuario(
        name ='Eduardo',
        username ='admin',
        is_admin =True
    )
    admin.set_password('admin')

    db.session.add(admin)
    db.session.commit()
