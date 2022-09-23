from flask import request
from flask_restful import Resource
from services.product_categories_service import ProductCategoryService
class ProductsCategoriesController(Resource):
    def __init__(self):
        self.service = ProductCategoryService()
    
    def get(self,version):
        return self.service.get_categories()
    
    def post(self,version):

        return self.service.add_category(request.get_json())
