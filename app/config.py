

# class Config:
#     USER='postgres'
#     PASS='admin'
#     HOST='localhost'
#     NAME_DB='TIENDA'
#     FULL_URL_DB = f'postgresql://{USER}:{PASS}@{HOST}/{NAME_DB}'

#     SECRET_KEY = 'llave_secreta'
#     SQLALCHEMY_DATABASE_URI = FULL_URL_DB
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
class Config:
    USER='postgres'
    PASS='admin'
    HOST='localhost'
    NAME_DB='TIENDA'
    DATABASE_URL = f'postgresql://{USER}:{PASS}@{HOST}/{NAME_DB}'

    SECRET_KEY = 'llave_secreta'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    