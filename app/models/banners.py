from sqlalchemy import inspect

from app.database import db


class Banners(db.Model):
    __tablename__ = 'banners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String)

    def __init__(self, name, image):
        # self.id = 1
        self.name = name
        self.image = image


    def __repr__(self):
        return f'{self.name} : {self.id}'

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
