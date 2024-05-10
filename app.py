from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

    from routes import register_routes
    register_routes(app)


    return app
