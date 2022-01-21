from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import VARCHAR
db = SQLAlchemy()

class MyModel(db.Model):
    id = db.Column(
        "id",
        VARCHAR,
        primary_key=True,
        unique=True,
        nullable=False,
    )

class MyObject(object):
    property = "some_property"