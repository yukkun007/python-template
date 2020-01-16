class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def past(self, year: int) -> None:
        self._age += year

    def show(self) -> None:
        print("私は{}。{}歳です。".format(self._name, self._age), end="")

    # プロパティ化
    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    name = property(get_name)
    age = property(get_age)
