def _get_message(param: str) -> str:
    return "Hello " + param


def message(text: str) -> None:
    print(_get_message("World!! You say {}.".format(text)), end="")
