import pytest
from BasicUnitTests.src.password import validate_password


def test_whole_password():
    assert validate_password("Password1234") == True

def test_password_has_uppercase():
    assert validate_password("Password1234") and validate_password("password1234") == False

def test_password_type():
    with pytest.raises(TypeError):
        validate_password(12345)
