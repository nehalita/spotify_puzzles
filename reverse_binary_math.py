import math

def get_binary_from_num(num_input, bin_num=0):
    if num_input == 0:
        return bin_num
    else:
        log2_base = int(math.log(num_input, 2))
        return get_binary_from_num(num_input - 2 ** log2_base, bin_num + 10 ** log2_base)

def reverse_number(num_input):
    return int("".join(reversed(str(num_input))))

def get_number_from_bin(num_input, dec_num=0):
    if num_input == 0:
        return dec_num
    else:
        log10_base = int(math.log10(num_input))
        return get_number_from_bin(num_input - 10 ** log10_base, dec_num + 2 ** log10_base)

def reverse_binary(num_input):
    bin_num = get_binary_from_num(num_input)
    rev_num = reverse_number(bin_num)
    rev_bin_num = get_number_from_bin(rev_num)
    return rev_bin_num

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
