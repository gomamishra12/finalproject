from flask import Flask
from chatapp.extensions import db, login_manager, bcrypt
from chatapp.config import Config
from chatapp.extensions import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # It's crucial to import and register Blueprints AFTER the extensions are initialized.
    with app.app_context():
        from chatapp.routes import main  # Adjusted to import the Blueprint
        app.register_blueprint(main)  # Registering the Blueprint
        db.create_all()

    return app

