import pytest
from app.cls.owner import Owner


class TestOwner:
    def setup(self):
        print("<<setup done>> ", end="")

    def tear_down(self):
        print(" <<tear_down done>>", end="")

    @pytest.fixture()
    def owner1(request):
        return Owner("Yutaka", 35, "Kanagawa")

    def test_past(self):
        o = Owner("Taro", 20, "Tokyo")
        o.past(15)
        assert o.name == "Taro"
        assert o.age == 35
        assert o.address == "Tokyo"

    def test_move(self, owner1):
        owner1.move("Nagoya")
        owner1.address == "Nagoya"

    def test_inner_move(self, owner1):
        owner1._inner_move("Nagoya")
        owner1.address == "Nagoya"

    def test_past_and_show(self, owner1):
        owner1.past(10)
        owner1.show()
        assert owner1.age == 45

    def test_direct_change(self, owner1):
        # 本当は変更手段を2つ用意すべきではない
        owner1.address = "Tokyo"
        assert owner1.address == "Tokyo"
