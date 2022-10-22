from flask import request
from flask_restful import Resource

from app.services.banners_service import BannersService


class BannersController(Resource):
    def __init__(self):
        self.name = 'Mahesh'
        self.service = BannersService()

    
    def get(self,version):

        return self.service.get_banners()
    def get(self,version):

        return self.service.get_banners()
    def get(self,version):

        return self.service.get_banners()
