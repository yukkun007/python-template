from app.cls.person import Person


class Owner(Person):
    def __init__(self, name: str, age: int, address: str) -> None:
        super().__init__(name, age)
        self._address = address

    def move(self, new_address: str) -> None:
        self._inner_move(new_address)

    # 非公開メソッド
    def _inner_move(self, new_address: str) -> None:
        self._address = new_address

    # オーバライド
    def show(self) -> None:
        print("私は所有者の{}。{}歳です。".format(self.name, self.age), end="")

    # プロパティ化
    def get_address(self) -> str:
        return self._address

    def set_address(self, address: str) -> None:
        self._address = address

    address = property(get_address, set_address)
