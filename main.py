from app.func import message
from app.cls.dog import Dog
from app.cls.owner import Owner


def main() -> None:
    message()
    print("")

    owner = Owner("Zagitova", 17, "rusia")
    dog = Dog("Masaru", owner)
    dog.show()


if __name__ == "__main__":
    main()
