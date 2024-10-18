from flask import Flask
from flask_cors import CORS
from routes.shopping_list_routes import shopping_list_bp
from utils.db import Base, engine

def create_app():
    app = Flask(__name__)

    app.register_blueprint(shopping_list_bp)

    Base.metadata.create_all(bind=engine)

    return app

app = create_app()


CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
