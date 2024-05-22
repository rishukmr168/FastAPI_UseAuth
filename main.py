from typing import Union
import re
from fastapi import FastAPI, Form, Request,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Models.items import Item
app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/",response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/register")
# async def register(username: str , password: str , email: str ):
async def register(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
    if ' ' in username:
        raise HTTPException(status_code=400, detail="Username cannot contain whitespace")
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    if not re.match(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*()-+]).*$', password):
        raise HTTPException(status_code=400, detail="Password must contain at least one number, one special character, and one uppercase or lowercase letter")
    if not email.endswith('@gmail.com'):
        raise HTTPException(status_code=400, detail="Invalid email format")
        # Return success message
    return {"message": "User registered successfully"}


# @app.post("/register")
# async def register(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
#     # Implement user registration logic here
#     if(check_validate_username(username)):
#         return {"message": "NO white Space allowed."}
#     if(validate_password(password)):
#         return {"message": "Try another Password"}
#     if (validate_password2(password)):
#         return {"message": "password contains at least one number, one special character, and one uppercase or lowercase letter"}
#     if(validate_email(email)):
#         return {"message": "Invalid Mail"}
#     # store in database
#     return {"message": "User registered successfully"}


def check_validate_username(username):
    # Check if there are any spaces in the username
    if ' ' in username:
        return True
    return False
def validate_password(password):
    # Check if password has minimum 8 characters
    if len(password) < 8:
        return True
    return False;
def validate_password2(password):
    # Check if password contains at least one number, one special character, and one uppercase or lowercase letter
    if not re.search(r'^(?=.*[0-9])(?=.*[!@#$%^&*()-+])(?=.*[a-zA-Z]).{8,}$', password):
        return True
    return False

def validate_email(email):
    # Check if email ends with '@gmail.com'
    if not email.endswith('@gmail.com'):
        return True
    return False


@app.post("/login")
def login(username: str , password: str ):
    if ' ' in username:
        raise HTTPException(status_code=400, detail="Username cannot contain whitespace")
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    if not re.match(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*()-+]).*$', password):
        raise HTTPException(status_code=400,detail="Password must contain at least one number, one special character, and one uppercase or lowercase letter")
    # If authentication succeeds, return user data
    # If authentication fails, raise HTTPException with status_code 401 (Unauthorized)
    return {"message": "Login successful"}


@app.get("/validate/{username}")
def validate(username):
    # Implement user validation logic here
    # If username exists, return user data
    # If username does not exist, raise HTTPException with status_code 404 (Not Found)
    return {"valid": True}  # For demonstration purposes, always return True


# @app.post("/login")
# def login(username: str, password: str):
#     return {"message": "Login successful"}
#
# @app.get("/validate/{username}")
# def validate(username: str):
#     # Implement user validation logic here
#     return {"valid": True}  # For demonstration purposes, always return True
