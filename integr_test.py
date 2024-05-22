import pytest
from main import check_validate_username, validate_password, validate_email

@pytest.mark.parametrize("username, expected", [
    ("valid_username", False),
    ("username with spaces", True),
])
def test_check_validate_username(username, expected):
    assert check_validate_username(username) == expected
#
@pytest.mark.parametrize("password, expected", [
    ("StrongPass123!", False),
    ("weak", True),
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected

@pytest.mark.parametrize("email, expected", [
    ("test@gmail.com", False),
    ("invalid-email", True),
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected
