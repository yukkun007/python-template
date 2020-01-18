def _get_message(param: str) -> str:
    return "Hello " + param


def message() -> None:
    print(_get_message("World!!"), end="")
