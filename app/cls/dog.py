from app.cls.owner import Owner


class Dog:
    def __init__(self, name: str, owner: Owner) -> None:
        self._name = name
        self._owner = owner

    def show(self) -> None:
        print("Bow wow.. I'm {}. My owner is {}.".format(self._name, self._owner.name), end="")

    # プロパティ化
    def get_name(self) -> str:
        return self._name

    name = property(get_name)
