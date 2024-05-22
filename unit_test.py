from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_register_valid():
    response = client.post(
        "/register",
        data={"username": "valid_username", "password": "valid123A@", "email": "valid@gmail.com"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_register_invalid_username():
    response = client.post(
        "/register",
        data={"username": "invalid username", "password": "invalid_password", "email": "invalid@gmail.com"},
    )
    assert response.status_code == 400
    assert response.json() == {'detail':"Username cannot contain whitespace"}

def test_register_invalid_password():
    response = client.post(
        "/register",
        data={"username": "valid_username", "password": "short", "email": "valid@gmail.com"},
    )
    assert response.status_code == 400
    assert response.json() == {'detail':"Password must be at least 8 characters long"}
def test_register_invalid_password2():
    response = client.post(
        "/register",
        data={"username": "valid_username", "password": "ahgagiHBWCIudciIU", "email": "valid@gmail.com"},
    )

    assert response.status_code == 400
    assert response.json() == {'detail':"Password must contain at least one number, one special character, and one uppercase or lowercase letter"}
def test_register_invalid_email():
    response = client.post(
        "/register",
        data={"username": "valid_username", "password": "PAssword@123", "email": "invalid_email"},
    )
    assert response.status_code == 400
    assert response.json() == {'detail':"Invalid email format"}


#




# from fastapi.testclient import TestClient
# from main import app
# client = TestClient(app)
#
#
# def test_register_valid():
#     response = client.post(
#         "/register",
#         data={"username": "valid_username", "password": "valid123A@", "email": "valid@gmail.com"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "User registered successfully"}
# def test_register_invalid_username():
#     response = client.post(
#         "/register",
#         data={"username": "invalid username", "password": "invalid_password", "email": "invalid@gmail.com"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "NO white Space allowed."}
# def test_register_invalid_password():
#     response = client.post(
#         "/register",
#         data={"username": "valid_username", "password": "short", "email": "valid@gmail.com"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "Try another Password"}
# def test_register_invalid_password2():
#     response = client.post(
#         "/register",
#         data={"username": "valid_username", "password": "ahgagiHBWCIudciIU", "email": "valid@gmail.com"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "password contains at least one number, one special character, and one uppercase or lowercase letter"}
# def test_register_invalid_email():
#     response = client.post(
#         "/register",
#         data={"username": "valid_username", "password": "PAssword@123", "email": "invalid_email"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "Invalid Mail"}
