from flask import Blueprint, request, jsonify
from .repository import UserRepository

user_bp = Blueprint('user_bp', __name__)
repo = UserRepository()

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = repo.get_all()
    
    if not users:
        return jsonify({
            "message": "No users found in the database.",
            "users": []
        }), 200
        
    return jsonify({
        "message": f"Successfully retrieved {len(users)} user(s).",
        "users": [u.to_dict() for u in users]
    }), 200

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = repo.get_by_id(id)
    
    if user:
        return jsonify({
            "message": f"User with ID {id} found successfully.",
            "user": user.to_dict()
        }), 200
    else:
        return jsonify({
            "message": f"User with ID {id} does not exist in our records.",
        }), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email'"}), 400
        
    try:
        user = repo.create(data['name'], data['email'])
        return jsonify({
            "message": "User created successfully!"
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    
    if not data or ('name' not in data and 'email' not in data):
        return jsonify({"error": "No data provided for update"}), 400
        
    updated_user = repo.update(id, data.get('name'), data.get('email'))
    
    if updated_user:
        return jsonify({
            "message": f"User {id} updated successfully!"
        }), 200
    else:
        return jsonify({
            "error": "User not found",
            "message": f"Could not update user {id} because they do not exist."
        }), 404 

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    success = repo.delete(id)

    if success:
        return jsonify({
            "message": f"User with ID {id} has been successfully deleted."
        }), 200
    else:
        return jsonify({
            "error": "User not found",
            "message": f"Could not delete user {id} because they do not exist."
        }), 404