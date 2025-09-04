from operations import conversion

def test_convert_to_decimal():
    assert conversion.convert_to_decimal("14") == 9
    assert conversion.convert_to_decimal("0") == 0
    assert conversion.convert_to_decimal("1") == 1
    assert conversion.convert_to_decimal("20") == 10
    assert conversion.convert_to_decimal("100") == 25
    assert conversion.convert_to_decimal("400") == 100

def test_convert_to_quinary():
    assert conversion.convert_to_quinary("9") == "14"
    assert conversion.convert_to_quinary("0") == ""
    assert conversion.convert_to_quinary("1") == "1"
    assert conversion.convert_to_quinary("10") == "20"
    assert conversion.convert_to_quinary("25") == "100"
    assert conversion.convert_to_quinary("100") == "400"