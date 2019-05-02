# content of test_sample.py
import pytest
from mathsfun import BasicMaths

bm = BasicMaths


class TestMaths(object):

    @pytest.mark.maths
    def test_add(self):
        assert bm.add(3, 4) == 7

    @pytest.mark.maths
    def test_subtract(self):
        assert bm.subtract(12, 7) == 5

    @pytest.mark.maths
    def test_divide(self):
        assert bm.divide(6, 2) == 3

    @pytest.mark.maths
    def test_floordiv(self):
        assert bm.floordiv(10, 3) == 3

    @pytest.mark.maths
    def test_exponent(self):
        assert bm.exponent(5, 2) == 25


class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    @pytest.mark.xfail
    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')


class TestTmpdir:

    @pytest.mark.xfail
    def test_needsfiles(tmpdir):
        print(tmpdir)
        assert 0
