from database import db
from sqlalchemy import inspect

categories = db.Table('categories',
    db.Column('category_id', db.Integer, db.ForeignKey('products_categories.product_category_id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String)
    image = db.Column(db.String)
    stock = db.Column(db.Integer)
    status = db.Column(db.String(2), default='AC')
    category_id = db.Column(db.Integer,db.ForeignKey('products_categories.product_category_id'),nullable=False)
    category = db.relationship("ProductCategories", back_populates="product", uselist=False)

    def __init__(self,  name, price, description, image, stock, status, category_id):
        # self.id = 1
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.stock = stock
        self.status = status
        self.categories = categories
        self.category_id = category_id
    def __repr__(self):

        return f'{self.name} : {self.id}'

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
       
class ProductCategories(db.Model):
    __tablename__ = 'products_categories'
    product_category_id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    product_category_name = db.Column(db.String(50))
    product_category_status = db.Column(db.String(2), default='AC')
    product_category_image = db.Column(db.String)
    product_category_description = db.Column(db.String)
    product = db.relationship("Product", back_populates="category")
    def __init__(self, product_category_name, product_category_status, product_category_image, product_category_description):
        # self.product_category_id = product_category_id
        self.product_category_name = product_category_name
        self.product_category_status = product_category_status
        self.product_category_image = product_category_image
        self.product_category_description = product_category_description
    
    def __repr__(self):
        return f'{self.product_category_name} : {self.product_category_id}'
    
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
