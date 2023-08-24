import hashlib
from flask import jsonify, request
import mysqlx
from app import app 
from model.signInsignup_model import SignupModel

# obj = SignupModel()


signup_model = SignupModel()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    result = signup_model.register_user(username, email, password)
    return jsonify(result)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    result = signup_model.login_user(username, password)
    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True)