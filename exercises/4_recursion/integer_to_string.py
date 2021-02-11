
def integer_to_string(number_in, base_in):
    convert_string = "0123456789ABCDEF"
    if number_in < base_in:
        return convert_string[number_in]
    else:
        return integer_to_string(number_in//base_in, base_in) + convert_string[number_in % base_in]


def reverse_string(string_in):
    if len(string_in) == 1:
        return string_in
    else:
        return reverse_string(string_in[1:]) + string_in[0]

