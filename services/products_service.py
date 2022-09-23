from models.products import Product
from database import db, baseUrl
from flask import jsonify


class ProductService():
    def __init__(self):
        self.something = 'nothing'
        self.db = db
    
    def get_products(self):
        data = []
        for row in Product.query.all():
            obj = row.toDict()
            obj['image'] = baseUrl+"/files/"+obj["image"] if obj["image"] else baseUrl+"/files/no-thumbnail.png"
            data.append(obj)
        return jsonify({
            'status': True,
            'message': 'Products',
            'data': data 
        })
    def add_product(self, payload):
        try:
            if not payload.get('name') or not payload.get('description') or not payload.get('price') or not payload.get('image') or not payload.get('stock') or not payload.get('category_id'):
                return jsonify({
                'status': False,
                'message': 'Required fields are not provided'
            })

            product = Product(name=payload.get('name'), description=payload.get('description'), price=payload.get('price'), image=payload.get('image'), stock=payload.get('stock'), status='AC',category_id=payload.get('category_id'))
            self.db.session.add(product)
            self.db.session.commit()
            return jsonify({
                'status': True,
                'message': 'Product added successfully',
                'lastId': product.id
            })
        except Exception as err:
            return jsonify({
                'status': False,
                'message': 'Unable to add product',
                'error': str(err)
            })


