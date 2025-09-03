from GUI import conversion

def add(a_quinary: str, b_quinary: str) -> str:
    a_dec = conversion.convert_to_decimal(a_quinary)
    b_dec = conversion.convert_to_decimal(b_quinary)
    result_dec = a_dec + b_dec
    return conversion.convert_to_quinary(str(result_dec))

def subtract(a_quinary: str, b_quinary: str) -> str:
    a_dec = conversion.convert_to_decimal(a_quinary)
    b_dec = conversion.convert_to_decimal(b_quinary)
    result_dec = a_dec - b_dec
    return conversion.convert_to_quinary(str(result_dec))

def multiply(a_quinary: str, b_quinary: str) -> str:
    a_dec = conversion.convert_to_decimal(a_quinary)
    b_dec = conversion.convert_to_decimal(b_quinary)
    result_dec = a_dec * b_dec
    return conversion.convert_to_quinary(str(result_dec))

def divide(a_quinary: str, b_quinary: str) -> str:
    a_dec = conversion.convert_to_decimal(a_quinary)
    b_dec = conversion.convert_to_decimal(b_quinary)
    if b_dec == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result_dec = a_dec // b_dec 
    return conversion.convert_to_quinary(str(result_dec))
