from operations import unary_ops

def test_square_with_quinary_input():
    assert unary_ops.square("3") == "14"

def test_square_root_with_quinary_input():
    assert unary_ops.square_root("14") == "3"

def test_square_root_edge_case():
    assert unary_ops.square_root("0") == "0"
    assert unary_ops.square_root("1") == "1"