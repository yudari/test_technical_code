from flask import Blueprint
from app.controllers.BilanganOperasiController import BilanganOperasiController

bilangan_operasi_route_blueprint = Blueprint('bilangan_operasi_route_api_v1', __name__, url_prefix='/api/v1/')

@bilangan_operasi_route_blueprint.route('/bilangan_operasi_route_api_v1/generate_segitiga', methods=["POST"])
def get_bilangan_segitiga():
    return BilanganOperasiController.createBilanganSegitiga()

@bilangan_operasi_route_blueprint.route('/bilangan_operasi_route_api_v1/generate_bilangan_ganjil', methods=["POST"])
def get_bilangan_ganjil():
    return BilanganOperasiController.createBilanganGanjil()

@bilangan_operasi_route_blueprint.route('/bilangan_operasi_route_api_v1/generate_bilangan_prima', methods=["POST"])
def get_bilangan_prima():
    return BilanganOperasiController.createBilanganPrima()