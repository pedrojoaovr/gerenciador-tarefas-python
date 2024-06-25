# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Define a página de login

    from app.models.user import User
    from app.models.task import Task

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    from app.routes.task_routes import task_bp
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)

    return app
