from flask import request
from flask_restful import Resource
from services.products_service import ProductService
class ProductsController(Resource):
    def __init__(self):
        self.name = 'Mahesh'
        self.service = ProductService()
    
    def get(self,version):

        return self.service.get_products(request.args)
    
    def post(self,version):

        return self.service.add_product(request.get_json())
