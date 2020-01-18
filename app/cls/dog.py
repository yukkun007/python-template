from app.cls.owner import Owner


class Dog:
    """
    犬の各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    name : str
        犬の名前。
    owner : Owner
        犬のオーナー。
    """

    def __init__(self, name: str, owner: Owner) -> None:
        """
        Parameters
        ----------
        name : str
            犬の名前。
        owner : Owner
            犬のオーナー。
        """
        self._name = name
        self._owner = owner

    def show(self) -> None:
        """
        犬の情報を表示する。
        """
        print("Bow wow.. I'm {}. My owner is {}.".format(self._name, self._owner.name), end="")

    @property
    def name(self) -> str:
        """
        犬の名前。
        """
        return self._name
