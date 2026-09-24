from pymongo import MongoClient
import hashlib


client = MongoClient("mongodb://localhost:27017/")
db = client["NoteSquid"]

def signUp(user, password):
    if db.users.find_one({"user": user}):
        return 'You already have an account! Make sure you click "log in" instead.'

    hashed = hashlib.sha256(password.encode()).hexdigest()
    db.users.insert_one({
        "user": user,
        "password": hashed,
        "joined": "2026-09-23"
    })

def login(user, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    user_doc = db.users.find_one({"user": user})

    if not user_doc:
        return False

    return user_doc["password"] == hashed
