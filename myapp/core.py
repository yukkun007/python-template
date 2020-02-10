from myapp.func import message
from myapp.cls.dog import Dog
from myapp.cls.owner import Owner


def do_something(text: str) -> None:
    message(text)


def do_anything(text: str) -> None:
    owner = Owner("Zagitova", 17, "rusia")
    dog = Dog("Masaru", owner)
    dog.show()
    print(" You say {}.".format(text))
