import pytest
from myapp.cls.dog import Dog
from myapp.cls.owner import Owner


class TestDog:
    @pytest.fixture()
    def dog1(request):
        owner = Owner("Zagitova", 17, "rusia")
        return Dog("Masaru", owner)

    def test_show(self, dog1: Dog):
        dog1.show()
        assert dog1.name == "Masaru"
