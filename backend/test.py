from fastapi import FastAPI, Form, HTTPException, Request
from typing import Annotated
import os
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import FileResponse , RedirectResponse
from fastapi import status

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

@app.post("/test")
async def login_user(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    db_connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = db_connection.cursor()

    query = "SELECT * FROM newestone.users WHERE email = %s"
    cursor.execute(query, (email,))
    data = cursor.fetchone()

    if not data:
        return FileResponse("../frontend/admin.html")
        
        cursor.close()
        db_connection.close()

    user_password_from_db = data[3]
   
    
    if user_password_from_db == password:
        return FileResponse("../frontend/db.html")
    else:
        return FileResponse("../frontend/admin.html")
        cursor.close()
        db_connection.close()
        
        



        
      