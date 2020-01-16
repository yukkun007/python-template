import pytest
from app.cls.person import Person


class TestPerson:
    def setup(self):
        print("<<setup done>> ", end="")

    def tear_down(self):
        print(" <<tear_down done>>", end="")

    @pytest.fixture()
    def person1(request):
        return Person("Yutaka", 35)

    def test_past(self):
        p = Person("Yutaka", 35)
        p.past(5)
        assert p.age == 40

    def test_show(self, person1):
        person1.show()

    def test_past_and_show(self, person1):
        person1.past(10)
        person1.show()
        assert person1.age == 45

    # setは出来ない
    def test_invalid_access(self, person1):
        with pytest.raises(AttributeError):
            person1.name = "Hoge"
