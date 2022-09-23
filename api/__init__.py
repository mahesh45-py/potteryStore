from flask import Blueprint
from flask_restful import Resource, Api
from controllers.products_controller import ProductsController
from controllers.products_categories_controller import ProductsCategoriesController
api_bp = Blueprint('api',__name__,url_prefix='/api/<version>')

api = Api(api_bp)
@api_bp.route('/')
def index(version):
    return 'FUCK IT - {}'.format(version)

    
api.add_resource(ProductsController,'/products')
api.add_resource(ProductsCategoriesController,'/productCategories')