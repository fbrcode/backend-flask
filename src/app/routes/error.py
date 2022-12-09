from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

error_bp = Blueprint("error", __name__)

@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    return jsonify({"message": "Something went wrong, please check the logs."}), 500

@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({"message": "Resource not found."}), 404
