import os
from flask import Flask, url_for, request, jsonify
from database import db
from api import api_bp
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import form
from jinja2.utils import markupsafe 
from models.products import Product, ProductCategories

basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'files')
database_path = os.path.join(basedir, 'data-dev.sqlite')

app = Flask(__name__, static_folder='files')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toystore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '@Mahesh2085'
app.config['SESSION_TYPE'] = 'filesystem'

db.init_app(app)
admin = Admin(app)

class ProductImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''

        return markupsafe.Markup(
            '<img src="%s">' %
            url_for('static',
                    filename=form.thumbgen_filename(model.image))
        )

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'image': form.ImageUploadField(
            'Product', base_path=file_path, thumbnail_size=(100, 100, True))
    }
class CategoriesImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.product_category_image:
            return ''

        return markupsafe.Markup(
            '<img src="%s">' %
            url_for('static',
                    filename=form.thumbgen_filename(model.product_category_image))
        )

    column_formatters = {
        'product_category_image': _list_thumbnail
    }

    form_extra_fields = {
        'product_category_image': form.ImageUploadField(
            'ProductCategories', base_path=file_path, thumbnail_size=(100, 100, True))
    }


admin.add_view(ProductImageView(Product,db.session))
admin.add_view(CategoriesImageView(ProductCategories,db.session))

app.register_blueprint(api_bp)



@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def method_name():
    return 'FUCK'

app.run(debug=True,port=8080)