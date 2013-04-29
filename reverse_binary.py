def get_binary_from_num(num_input):
    full_bin = bin(num_input)
    return full_bin[2:]

def reverse_number(num_input):
    num_str = ""
    for digit in reversed(num_input):
        num_str += digit
    return num_str

def get_number_from_bin(num_input):
    return int(num_input,2)

def reverse_binary(num_input):
    bin_str = get_binary_from_num(num_input)
    rev_str = reverse_number(bin_str)
    rev_bin_num = get_number_from_bin(rev_str)
    return rev_bin_num

assert get_binary_from_num(0) == '0'
assert get_binary_from_num(1) == '1'
assert get_binary_from_num(2) == '10'
assert get_binary_from_num(3) == '11'
assert get_binary_from_num(4) == '100'
assert get_binary_from_num(5) == '101'
assert get_binary_from_num(13) == '1101'
assert get_binary_from_num(133) == '10000101'

assert reverse_number('4321') == '1234'

assert get_number_from_bin('10000101') == 133

assert reverse_binary(13) == 11
assert reverse_binary(47) == 61
