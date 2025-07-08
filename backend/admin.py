from fastapi import FastApi

app = FastApi

app.get("../frontend/admin.html")
async def adminPage(){  
    return 
}