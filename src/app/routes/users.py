from flask import Blueprint, jsonify, request, Response

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["GET"])
def get_users():
  users = [{"name": "John Doe"}, {"name": "Jane Doe"}]
  return jsonify(users)

@users_bp.route("", methods=["POST"])
def create_user():
  data = request.json
  print(data)
  return Response(status=204)
  # or...
  # return jsonify(data), 201
