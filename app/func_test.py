import pytest
from app.func import _get_message, message


class TestFunc:
    def test_get_message(self):
        result = _get_message("World")
        assert result == "Hello World"

    @pytest.mark.parametrize("input, expected", [("Foo", "Hello Foo"), ("Bar", "Hello Bar")])
    def test_get_message_param(self, input, expected):
        result = _get_message(input)
        assert result == expected

    def test_message(self):
        message()
