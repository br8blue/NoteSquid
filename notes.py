from db import db
from datetime import datetime
from bson import ObjectId



def createNote(user, noteTitle, noteContent):
    db.notes.insert_one({
        "user": user,
        "title": noteTitle,
        "content": noteContent,
        "noteCreated": datetime.now().strftime("%Y-%m-%d"),
        "noteUpdated": datetime.now().strftime("%Y-%m-%d")
    })


def getNotes(user):
    return list(db.notes.find({"user": user}))


def updateNote(noteId, noteContent):
    db.notes.update_one(
        {"_id": ObjectId(noteId)},
        {"$set": {
            "content": noteContent,
            "noteUpdated": datetime.now().strftime("%Y-%m-%d")
        }}
    )




def deleteNote(noteId):
    db.notes.delete_one(
        {"_id": ObjectId(noteId)}
    )