from app.cls.person import Person


class Owner(Person):
    """
    オーナーの各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    name : str
        オーナーの名前。
    age : int
        オーナーの年齢。
    address : str
        オーナーの住所。
    """

    def __init__(self, name: str, age: int, address: str) -> None:
        """
        Parameters
        ----------
        name : str
            オーナーの名前。
        age : int
            オーナーの年齢。
        address : str
            オーナーの住所。
        """
        super().__init__(name, age)
        self._address = address

    def move(self, new_address: str) -> None:
        """
        オーナーの住所を更新する。

        Parameters
        ----------
        new_address : str
            新しい住所。

        See Also
        ----------
            __inner_move : オーナーの住所を更新する（非公開メソッド）。
        """
        self._inner_move(new_address)

    def _inner_move(self, new_address: str) -> None:
        """
        オーナーの住所を更新する。

        Parameters
        ----------
        new_address : str
            新しい住所。

        Notes
        ----------
            非公開メソッド。
        """
        self._address = new_address

    def show(self) -> None:
        """
        オーナーの情報を表示する。

        Notes
        ----------
            オーバライドしている。
        """
        print("私は所有者の{}。{}歳です。".format(self.name, self.age), end="")

    @property
    def address(self) -> str:
        """
        Returns
        -------
        str
            オーナーの住所。
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Parameters
        ----------
        address : str
            オーナーの住所。
        """
        self._address = address
