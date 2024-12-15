#submit50 cs50/problems/2022/python/tests/bank
from bank import value

def test_value():
    assert value("cat")== "$100"

if __name__ == "__main__":
    test_value()
