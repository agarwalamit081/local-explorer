from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management

    # Register the main_routes blueprint
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
