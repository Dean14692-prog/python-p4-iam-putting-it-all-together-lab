# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy.orm import validates
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin
# from flask_bcrypt import Bcrypt

# convention = {
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_%(constraint_name)s",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s"
# }

# metadata = MetaData(naming_convention=convention)
# db = SQLAlchemy(metadata=metadata)
# bcrypt = Bcrypt()

# class User(db.Model, SerializerMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     _password_hash = db.Column(db.String)
#     image_url = db.Column(db.String)
#     bio = db.Column(db.String)

#     recipes = db.relationship('Recipe', backref='user', cascade='all, delete-orphan')
#     serialize_rules = ('-recipes.user', '-_password_hash')

#     @property
#     def password_hash(self):
#         raise AttributeError('Password hashes may not be viewed.')

#     @password_hash.setter
#     def password_hash(self, password):
#         password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
#         self._password_hash = password_hash.decode('utf-8')

#     def authenticate(self, password):
#         return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

#     @validates('username')
#     def validate_username(self, key, username):
#         if not username:
#             raise ValueError("Username is required")
#         if len(username) < 3:
#             raise ValueError("Username must be at least 3 characters")
#         return username

# class Recipe(db.Model, SerializerMixin):
#     __tablename__ = 'recipes'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     instructions = db.Column(db.String, nullable=False)
#     minutes_to_complete = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     serialize_rules = ('-user.recipes',)

#     @validates('title')
#     def validate_title(self, key, title):
#         if not title:
#             raise ValueError("Title is required")
#         if len(title) < 3:
#             raise ValueError("Title must be at least 3 characters")
#         return title

#     @validates('instructions')
#     def validate_instructions(self, key, instructions):
#         if not instructions:
#             raise ValueError("Instructions are required")
#         if len(instructions) < 50:
#             raise ValueError("Instructions must be at least 50 characters long")
#         return instructions

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    recipes = db.relationship('Recipe', backref='user', cascade='all, delete-orphan')
    serialize_rules = ('-recipes.user', '-_password_hash')

    @property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username is required")
        if User.query.filter_by(username=username).first():
            raise ValueError("Username must be unique")
        return username

class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    minutes_to_complete = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    serialize_rules = ('-user.recipes',)

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title is required")
        return title

    @validates('instructions')
    def validate_instructions(self, key, instructions):
        if not instructions:
            raise ValueError("Instructions are required")
        if len(instructions) < 50:
            raise ValueError("Instructions must be at least 50 characters long")
        return instructions