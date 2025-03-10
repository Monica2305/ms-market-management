# user_controller.py (Controller)
from Service.user_service import create_user
from flask import request, jsonify

def create_user_controller():
    user_data = request.get_json()
    user = create_user(db_session, user_data)
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201