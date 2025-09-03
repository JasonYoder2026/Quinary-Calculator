import pytest
from operations import binary_ops

def test_addition():
    assert binary_ops.add("3", "2") == "10"  
    assert binary_ops.add("14", "1") == "20"

def test_subtraction():
    assert binary_ops.subtract("4", "2") == "2"  
    assert binary_ops.subtract("10", "3") == "2" 

def test_multiplication():
    assert binary_ops.multiply("2", "3") == "11"  
    assert binary_ops.multiply("4", "4") == "31" 

def test_division():
    assert binary_ops.divide("10", "2") == "2" 
    assert binary_ops.divide("14", "3") == "3"  

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        binary_ops.divide("10", "0")
