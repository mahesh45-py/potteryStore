from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
# baseUrl = "http://localhost:8080"
baseUrl = "http://192.168.41.230:5000"
# baseUrl = "https://mahesh54.pythonanywhere.com"
