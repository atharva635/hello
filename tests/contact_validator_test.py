import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone

def test_is_valid_email_true():
    """Test a well-formed email."""
    email = "student@lpu.in"
    result = is_valid_email(email)
    assert result == True

def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)

def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    phone = "555-123-4567"
    result = is_valid_phone(phone)
    assert result == True

def test_mask_email_basic():
    """Test masking a typical email address."""
    email = "priya@example.com"

    result = mask_email(email)

    assert result == "pr***@example.com"

def test_normalize_phone():
    """Test that normalize_phone removes dashes."""
    phone = "555-123-4567"

    result = normalize_phone(phone)

    assert result == "5551234567"

def test_is_valid_phone_type_error():
    with pytest.raises(TypeError):
        is_valid_phone(12345)


def test_mask_email_invalid():
    with pytest.raises(ValueError):
        mask_email("invalid-email")


def test_mask_email_short_local():
    result = mask_email("ab@example.com")
    assert result == "a*@example.com"


def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("123")
