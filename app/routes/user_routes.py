from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.models.user_model import serialize_user

user_bp = Blueprint('users', __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([serialize_user(u) for u in users]), 200

@user_bp.route("/<id>", methods=["GET"])
def get_user(id):
    user = UserService.get_user(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(serialize_user(user)), 200

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    result = UserService.create_user(data)
    return jsonify({"id": str(result.inserted_id)}), 201

@user_bp.route("/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    result = UserService.update_user(id, data)
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated"}), 200

@user_bp.route("/<id>", methods=["DELETE"])
def delete_user(id):
    result = UserService.delete_user(id)
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200
