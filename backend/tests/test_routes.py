"""Test route handlers for FastAPI application."""


def test_fail() -> None:
    """Test that will fail."""
    var = 1
    var_2 = 1
    assert var == var_2
