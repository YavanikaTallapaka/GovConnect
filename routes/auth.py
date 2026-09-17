from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/register")
def register(name: str, email: str, password: str, role: str):

    conn = sqlite3.connect("govconnect.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",
        (name, email, password, role)
    )

    conn.commit()
    conn.close()

    return {"message": "User Registered Successfully"}

@router.post("/login")
def login(email: str, password: str):

    conn = sqlite3.connect("govconnect.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {"message": "Login Successful"}

    return {"message": "Invalid Email or Password"}