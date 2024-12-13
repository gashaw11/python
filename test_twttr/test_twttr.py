#submit50 cs50/problems/2022/python/tests/twttr

from twttr import shorten


def test_shorten():
    assert shorten("Hello")=="hll"
