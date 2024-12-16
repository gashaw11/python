#submit50 cs50/problems/2022/python/tests/plates
from plates import is_valid

def test_plates():
    assert is_valid("12AVB")==False
    assert is_valid("D2AVB")==False
    assert is_valid("FGGGGAVB")==False

if __name__=="__main__":
    test_plates()
