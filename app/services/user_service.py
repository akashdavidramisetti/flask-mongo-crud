from bson import ObjectId
from flask import current_app

class UserService:
    @staticmethod
    def get_all_users():
        return list(current_app.db.users.find())

    @staticmethod
    def get_user(user_id):
        return current_app.db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def create_user(data):
        return current_app.db.users.insert_one(data)

    @staticmethod
    def update_user(user_id, data):
        return current_app.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete_user(user_id):
        return current_app.db.users.delete_one({"_id": ObjectId(user_id)})
