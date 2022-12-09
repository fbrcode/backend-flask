# from flask import jsonify, request, Response
from src.app import create_app

app = create_app()

# run as a module
if __name__ == "__main__":
    app.run(host="127.0.0.1")
    