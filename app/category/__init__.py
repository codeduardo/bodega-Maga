from flask import Blueprint

category = Blueprint('category',__name__ ,url_prefix='/category', template_folder = 'templates' )

from . import views