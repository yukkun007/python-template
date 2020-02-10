from myapp.core import do_something, do_anything


class TestCore:
    def test_do_something(self):
        do_something("Foo")

    def test_do_anything(self):
        do_anything("Bar")
