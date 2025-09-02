def convert_to_decimal(num_as_str):
    decimal_value = int(num_as_str,5)
    return decimal_value

def convert_to_quinary(num_as_str):
    final_value = ""
    quinary_value = int(num_as_str)
    while quinary_value > 0:
        remainder = quinary_value % 5
        final_value = str(remainder) + final_value
        quinary_value = quinary_value // 5
        
    return final_value