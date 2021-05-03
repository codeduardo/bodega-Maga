

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
    DATABASE_URL = 'postgres://fbzesginhgxytp:7c5c2ce2a868e7c8330d07188ae9a6ab8c126f43fe823859c85f55c63e6d13b3@ec2-3-217-219-146.compute-1.amazonaws.com:5432/d80so7bhl4ra3h'

    SECRET_KEY = 'llave_secreta'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    