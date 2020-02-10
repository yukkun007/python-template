class Person:
    """
    人の各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    name : str
        人の名前。
    age : int
        人の年齢。
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Parameters
        ----------
        name : str
            人の名前。
        age : int
            人の年齢。
        """
        self._name = name
        self._age = age

    def past(self, year: int) -> None:
        """
        加齢。

        Parameters
        ----------
        year : int
            経過した年数。
        """
        self._age += year

    def show(self) -> None:
        """
        人の情報を表示する。
        """
        print("私は{}。{}歳です。".format(self._name, self._age), end="")

    @property
    def name(self) -> str:
        """
        Returns
        -------
        str
            人の名前。
        """
        return self._name

    @property
    def age(self) -> int:
        """
        Returns
        -------
        int
            人の年齢。
        """
        return self._age
