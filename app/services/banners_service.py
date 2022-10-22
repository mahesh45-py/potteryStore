from flask import jsonify

from app.database import baseUrl
from app.models.banners import Banners


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
