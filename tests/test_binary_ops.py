import pytest
from operations import binary_ops

def test_addition():
    assert binary_ops.add("3", "2") == "10"  

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        binary_ops.divide("10", "0")
