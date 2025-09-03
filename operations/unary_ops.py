from GUI import conversion 

def square(num_quinary_as_str):
    decimal_value = conversion.convert_to_decimal(num_quinary_as_str)
    square_value = decimal_value ** 2
    return conversion.convert_to_quinary(str(square_value))

def square_root(num_quinary_as_str):
    decimal_value = conversion.convert_to_decimal(num_quinary_as_str)
    square_root_value = int(decimal_value ** 0.5)
    return conversion.convert_to_quinary(str(square_root_value))
