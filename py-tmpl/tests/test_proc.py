from src.proc import Hello


def test_print():
    assert Hello().print() == 'Hello World!!'
