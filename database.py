from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
# baseUrl = "http://localhost:8080"
# baseUrl = "http://192.168.41.230:5000"
baseUrl = "https://mahesh54.pythonanywhere.com"
