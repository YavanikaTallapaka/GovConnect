from fastapi import APIRouter
from models.complaint import Complaint, StatusUpdate
import sqlite3

router = APIRouter()

@router.post("/complaints")
def create_complaint(complaint: Complaint):

    conn = sqlite3.connect("govconnect.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO complaints
        (title, description, category, location, user_id)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            complaint.title,
            complaint.description,
            complaint.category,
            complaint.location,
            complaint.user_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "Complaint Submitted Successfully"}


@router.get("/complaints")
def get_complaints():

    conn = sqlite3.connect("govconnect.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")

    complaints = cursor.fetchall()

    conn.close()

    return complaints

@router.put("/complaints/{complaint_id}")
def update_status(complaint_id: int, update: StatusUpdate):

    conn = sqlite3.connect("govconnect.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE complaints SET status=? WHERE id=?",
        (update.status, complaint_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Status Updated Successfully"}