from flask import Flask, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.routes import bilangan_operasi_route

@app.route('/', methods=['GET'])
def index_app():
    return jsonify({'status_code': 200, 'message': "Test Application Sucess Call Api"})


app.register_blueprint(bilangan_operasi_route.bilangan_operasi_route_blueprint)
