import sys
sys.path.append('D:\Google\Python\Website-with-Bootstrap')
import try_this
import pytest


@pytest.mark.parametrize('a, b, exected_result', [(5,5,1),(10,2,5),(20,-5,-4), (5,2,2.5)])
def test_division(a, b, exected_result):
    assert try_this.division_func(a, b) == exected_result

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        try_this.division_func(20, 0)