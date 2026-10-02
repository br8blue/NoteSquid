from db import db
from datetime import datetime
from bson import ObjectId


def createChecklist(user, checklistTitle):
    db.checklists.insert_one({
        "user": user,
        "title": checklistTitle,
        "checklistCreated": datetime.now().strftime("%Y-%m-%d"),
        "checklistUpdated": datetime.now().strftime("%Y-%m-%d")
    })

def updateChecklist(checklistId, checklistTitle):
    db.checklists.update_one(
        {"_id": ObjectId(checklistId)},
        {"$set": {
            "title": checklistTitle,
            "checklistUpdated": datetime.now().strftime("%Y-%m-%d")
        }}
    )

def deleteChecklist(checklistId):
    db.checklists.delete_one(
        {"_id": ObjectId(checklistId)}
    )