from models.banners import Banners
from database import baseUrl
from flask import jsonify


class BannersService():
    def __init__(self):
        self.something = 'nothing'
    
    def get_banners(self):
        data = []
        result= Banners.query.all()
        for row in result:
            
            obj = row.toDict()
            obj['image'] = baseUrl+"/files/"+obj["image"] if obj["image"] else baseUrl+"/files/no-thumbnail.png"
            data.append(obj)
        return jsonify({
            'status': True,
            'message': 'Banners',
            'data': data 
        })
