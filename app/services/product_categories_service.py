from flask import jsonify

from app.database import baseUrl, db
from app.models.products import Product, ProductCategories


class ProductCategoryService():
    def __init__(self):
        self.db = db
    def get_categories(self):
        data = []
        for row in ProductCategories.query.all():
            obj = row.toDict()
            obj['product_category_image'] = baseUrl+"/files/"+obj["product_category_image"] if obj["product_category_image"] else baseUrl+"/files/no-thumbnail.png"
            data.append(obj)
        return jsonify({
            'status': True,
            'message': 'Product Categories',
            'data': data
        })

    def add_category(self, payload):
        try:
            if not payload.get('name') or not payload.get('image'):
                return jsonify({
                'status': False,
                'message': 'Required fields are not provided'
            })

            category = ProductCategories(product_category_name=payload.get('name'), product_category_image=payload.get('image'), product_category_status='AC')
            self.db.session.add(category)
            self.db.session.commit()
            return jsonify({
                'status': True,
                'message': 'Product Category added successfully',
                'lastId': category.product_category_id
            })
        except Exception as err:
            return jsonify({
                'status': False,
                'message': 'Unable to add Product Category',
                'error': str(err)
            })

