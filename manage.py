import logging.handlers
import os

from flask import Flask, jsonify, request, url_for
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from jinja2.utils import markupsafe

from api import api_bp
from database import db, mail, migrate
from models.banners import Banners
from models.products import Product, ProductCategories

basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'files')
database_path = os.path.join(basedir, 'data-dev.sqlite')

app = Flask(__name__, static_folder='files')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toystore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '@Mahesh2085'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'srikakulammahesh2085@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'srikakulammahesh2085@gmail.com'
app.config['MAIL_PASSWORD'] = 'lhtlnrbkmenpgdcd'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db.init_app(app)
migrate.init_app(app,db)
mail.init_app(app)
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

class BannerImageView(ModelView):
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
            'Banners', base_path=file_path, thumbnail_size=(100, 100, True))
    }

admin.add_view(ProductImageView(Product,db.session))
admin.add_view(CategoriesImageView(ProductCategories,db.session))
admin.add_view(BannerImageView(Banners,db.session))
app.register_blueprint(api_bp)



@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def method_name():
    return 'FUCK'

def setup_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    
    file_name = os.path.join("log", 'POTTERY_STORE_{}.log'.format("api_log"))
    file_handler = logging.handlers.TimedRotatingFileHandler(file_name, when='d', backupCount=7)
    
    root.addHandler(file_handler)


setup_logger()

# app.run(debug=True,port=8080)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
