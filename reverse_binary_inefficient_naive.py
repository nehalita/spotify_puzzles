import sys

def get_binary_from_num(num_input):
    bin_num = 0
    for count in range(num_input):
        bin_num = inc_binary(bin_num)
    return bin_num

def inc_binary(num_input):
    if num_input % 10 == 0:
        return num_input + 1
    else:
        return inc_binary(num_input / 10) * 10

def reverse_number(num_input):
    num_string = ""
    for digit in reversed(str(num_input)):
        num_string += digit
    return int(num_string)

def get_number_from_bin(num_input):
    counter = 0
    while num_input > 0:
        num_input = dec_binary(num_input)
        counter += 1
    return counter

def dec_binary(num_input):
    if num_input % 10 == 1:
        return num_input - 1
    else:
        return dec_binary(num_input / 10) * 10 + 1

def reverse_binary(num_input):
    bin_num = get_binary_from_num(num_input)
    rev_num = reverse_number(bin_num)
    rev_bin_num = get_number_from_bin(rev_num)
    return rev_bin_num

def test_binary_program():
    assert get_binary_from_num(0) == 0
    assert get_binary_from_num(1) == 1
    assert get_binary_from_num(2) == 10
    assert get_binary_from_num(3) == 11
    assert get_binary_from_num(4) == 100
    assert get_binary_from_num(5) == 101
    assert get_binary_from_num(13) == 1101
    assert get_binary_from_num(133) == 10000101

    assert reverse_number(4321) == 1234

    assert get_number_from_bin(10000101) == 133

    assert reverse_binary(13) == 11
    assert reverse_binary(47) == 61

if __name__ == '__main__':
    input_int = int(sys.stdin.read())
    print get_binary_from_num(input_int)
