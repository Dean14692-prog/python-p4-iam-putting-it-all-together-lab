

# # from flask import Flask, request, make_response, session
# # from flask_restful import Api, Resource
# # from flask_migrate import Migrate
# # from flask_cors import CORS
# # from models import db, User, Recipe
# # import os

# # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # DATABASE = os.environ.get(
# #     "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.json.compact = False
# # app.secret_key = os.environ.get('SECRET_KEY', 'development-key')

# # migrate = Migrate(app, db)
# # db.init_app(app)
# # api = Api(app)
# # CORS(app, supports_credentials=True)

# # class Signup(Resource):
# #     def post(self):
# #         data = request.get_json()
        
# #         # Check for required fields
# #         if not data or 'username' not in data or 'password' not in data:
# #             return make_response({'errors': ['Username and password are required']}, 422)
        
# #         try:
# #             new_user = User(
# #                 username=data.get('username'),
# #                 image_url=data.get('image_url', ''),
# #                 bio=data.get('bio', '')
# #             )
# #             new_user.password_hash = data['password']
            
# #             db.session.add(new_user)
# #             db.session.commit()
            
# #             session['user_id'] = new_user.id
            
# #             return make_response(new_user.to_dict(), 201)
        
# #         except ValueError as e:
# #             db.session.rollback()
# #             return make_response({'errors': [str(e)]}, 422)

# # class CheckSession(Resource):
# #     def get(self):
# #         user_id = session.get('user_id')
# #         if not user_id:
# #             return make_response({'error': 'Unauthorized'}, 401)
        
# #         user = User.query.filter_by(id=user_id).first()
# #         if not user:
# #             return make_response({'error': 'Unauthorized'}, 401)
            
# #         return make_response(user.to_dict(), 200)

# # class Login(Resource):
# #     def post(self):
# #         data = request.get_json()
# #         username = data.get('username')
# #         password = data.get('password')
        
# #         if not username or not password:
# #             return make_response({'error': 'Username and password are required'}, 401)
        
# #         user = User.query.filter_by(username=username).first()
        
# #         if user and user.authenticate(password):
# #             session['user_id'] = user.id
# #             return make_response(user.to_dict(), 200)
        
# #         return make_response({'error': 'Invalid username or password'}, 401)

# # class Logout(Resource):
# #     def delete(self):
# #         if 'user_id' not in session:
# #             return make_response({'error': 'Unauthorized'}, 401)
            
# #         session.pop('user_id')
# #         return make_response({}, 204)

# # class RecipeIndex(Resource):
# #     def get(self):
# #         if 'user_id' not in session:
# #             return make_response({'error': 'Unauthorized'}, 401)
            
# #         recipes = Recipe.query.all()
# #         return make_response([recipe.to_dict() for recipe in recipes], 200)
    
# #     def post(self):
# #         if 'user_id' not in session:
# #             return make_response({'error': 'Unauthorized'}, 401)
            
# #         data = request.get_json()
        
# #         try:
# #             new_recipe = Recipe(
# #                 title=data.get('title'),
# #                 instructions=data.get('instructions'),
# #                 minutes_to_complete=data.get('minutes_to_complete'),
# #                 user_id=session['user_id']
# #             )
            
# #             db.session.add(new_recipe)
# #             db.session.commit()
            
# #             return make_response(new_recipe.to_dict(), 201)
        
# #         except ValueError as e:
# #             db.session.rollback()
# #             return make_response({'errors': [str(e)]}, 422)

# # api.add_resource(Signup, '/signup')
# # api.add_resource(CheckSession, '/check_session')
# # api.add_resource(Login, '/login')
# # api.add_resource(Logout, '/logout')
# # api.add_resource(RecipeIndex, '/recipes')

# # if __name__ == '__main__':
# #     app.run(port=5555, debug=True)


# from flask import Flask, request, make_response, session
# from flask_restful import Api, Resource
# from flask_migrate import Migrate
# from flask_cors import CORS
# from models import db, User, Recipe
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get(
#     "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
# app.secret_key = os.environ.get('SECRET_KEY', 'development-key')

# migrate = Migrate(app, db)
# db.init_app(app)
# api = Api(app)
# CORS(app, supports_credentials=True)

# class Signup(Resource):
#     def post(self):
#         data = request.get_json()
        
#         if not data or 'username' not in data or 'password' not in data:
#             return make_response({'errors': ['Username and password are required']}, 422)
        
#         try:
#             new_user = User(
#                 username=data['username'],
#                 image_url=data.get('image_url', ''),
#                 bio=data.get('bio', '')
#             )
#             new_user.password_hash = data['password']
            
#             db.session.add(new_user)
#             db.session.commit()
            
#             session['user_id'] = new_user.id
#             return make_response(new_user.to_dict(), 201)
        
#         except ValueError as e:
#             db.session.rollback()
#             return make_response({'errors': [str(e)]}, 422)

# class CheckSession(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if not user_id:
#             return make_response({'error': 'Unauthorized'}, 401)
        
#         user = User.query.get(user_id)
#         if not user:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         return make_response(user.to_dict(), 200)

# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')
        
#         if not username or not password:
#             return make_response({'error': 'Username and password are required'}, 401)
        
#         user = User.query.filter_by(username=username).first()
        
#         if user and user.authenticate(password):
#             session['user_id'] = user.id
#             return make_response(user.to_dict(), 200)
        
#         return make_response({'error': 'Invalid username or password'}, 401)

# class Logout(Resource):
#     def delete(self):
#         if 'user_id' not in session:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         session.pop('user_id')
#         return make_response({}, 204)

# class RecipeIndex(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if not user_id:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         user = User.query.get(user_id)
#         if not user:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         recipes = Recipe.query.all()
#         return make_response([recipe.to_dict() for recipe in recipes], 200)
    
#     def post(self):
#         user_id = session.get('user_id')
#         if not user_id:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         user = User.query.get(user_id)
#         if not user:
#             return make_response({'error': 'Unauthorized'}, 401)
            
#         data = request.get_json()
        
#         try:
#             new_recipe = Recipe(
#                 title=data['title'],
#                 instructions=data['instructions'],
#                 minutes_to_complete=data['minutes_to_complete'],
#                 user_id=user_id
#             )
            
#             db.session.add(new_recipe)
#             db.session.commit()
            
#             return make_response(new_recipe.to_dict(), 201)
        
#         except ValueError as e:
#             db.session.rollback()
#             return make_response({'errors': [str(e)]}, 422)

# api.add_resource(Signup, '/signup')
# api.add_resource(CheckSession, '/check_session')
# api.add_resource(Login, '/login')
# api.add_resource(Logout, '/logout')
# api.add_resource(RecipeIndex, '/recipes')

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

from flask import Flask, request, make_response, session
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Recipe
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = os.environ.get('SECRET_KEY', 'development-key')

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)
CORS(app, supports_credentials=True)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return make_response({'errors': ['Username and password are required']}, 422)
        
        try:
            new_user = User(
                username=data['username'],
                image_url=data.get('image_url', ''),
                bio=data.get('bio', '')
            )
            new_user.password_hash = data['password']
            
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            return make_response(new_user.to_dict(), 201)
        
        except ValueError as e:
            db.session.rollback()
            return make_response({'errors': [str(e)]}, 422)

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return make_response({'error': 'Unauthorized'}, 401)
        
        user = db.session.get(User, user_id)
        if not user:
            return make_response({'error': 'Unauthorized'}, 401)
            
        return make_response(user.to_dict(), 200)

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return make_response({'error': 'Username and password are required'}, 401)
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)
        
        return make_response({'error': 'Invalid username or password'}, 401)

class Logout(Resource):
    def delete(self):
        if not session.get('user_id'):
            return make_response({'error': 'Unauthorized'}, 401)
            
        session.pop('user_id', None)
        return make_response({}, 204)

class RecipeIndex(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return make_response({'error': 'Unauthorized'}, 401)
            
        user = db.session.get(User, user_id)
        if not user:
            return make_response({'error': 'Unauthorized'}, 401)
            
        recipes = Recipe.query.all()
        return make_response([recipe.to_dict() for recipe in recipes], 200)
    
    def post(self):
        user_id = session.get('user_id')
        if not user_id:
            return make_response({'error': 'Unauthorized'}, 401)
            
        user = db.session.get(User, user_id)
        if not user:
            return make_response({'error': 'Unauthorized'}, 401)
            
        data = request.get_json()
        
        try:
            new_recipe = Recipe(
                title=data['title'],
                instructions=data['instructions'],
                minutes_to_complete=data['minutes_to_complete'],
                user_id=user_id
            )
            
            db.session.add(new_recipe)
            db.session.commit()
            
            return make_response(new_recipe.to_dict(), 201)
        
        except ValueError as e:
            db.session.rollback()
            return make_response({'errors': [str(e)]}, 422)

api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(RecipeIndex, '/recipes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)