from http import HTTPStatus

from flask import Blueprint, request, jsonify
from services.predict_service import *

PREDICT_URL = '/api/predict'
predict_blueprint = Blueprint('student', __name__, url_prefix=PREDICT_URL)

@predict_blueprint.route("/url", methods=["POST"])
def predict_url():
    data = request.get_json()
    if data is None:
        return jsonify({"message": "No input data provided"}), 400

    url = data['url']

    if url is None:
        return jsonify({"message": "No url provided"}), 400

    res = predict_url(url)

    if "error" in res:
        return jsonify({"message": res["error"]}), 400

    return jsonify(res), HTTPStatus.OK
