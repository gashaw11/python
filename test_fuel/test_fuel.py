#submit50 cs50/problems/2022/python/fuel

from fuel import gauge, convert

def test_fuel():
    assert gauge(100)=="F"
    assert convert("3/4")==75.0
if __name__=="__main__":
      test_fuel()
