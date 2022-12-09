from flask import jsonify, request, Response
from src.app import create_app

app = create_app()

@app.route("/health", methods=["GET"])
def health_check():
    return "OK"

@app.route("/users", methods=["GET"])
def get_users():
  users = [{"name": "John Doe"}, {"name": "Jane Doe"}]
  return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
  data = request.json
  print(data)
  return Response(status=204)
  # or...
  # return jsonify(data), 201

# run as a module
if __name__ == "__main__":
    app.run(host="127.0.0.1")
    