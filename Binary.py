
def decimal_to_binary_list(num, bit_size=8):
    """Helper to convert decimal to a fixed-width binary list (LSB first)."""
    bits = []
    temp = abs(num)
    for _ in range(bit_size):
        bits.append(temp % 2)
        temp //= 2
    return bits

def add_bit_lists(list1, list2):
    """Adds two binary lists (LSB first) and returns the result (MSB first)."""
    result = []
    carry = 0
    for i in range(len(list1)):
        total = list1[i] + list2[i] + carry
        result.append(total % 2)
        carry = total // 2
    return result[::-1]

def Binary_negation(number, bit_size=8):
    """Returns the two's complement of a number as a list (LSB first)."""
    pos_bits = decimal_to_binary_list(abs(number), bit_size)
    neg_bits = []
    found_first_one = False
    
    for bit in pos_bits:
        if not found_first_one:
            neg_bits.append(bit)
            if bit == 1:
                found_first_one = True
        else:
            # Flip the bits after the first '1'
            neg_bits.append(1 if bit == 0 else 0)
    return neg_bits

def Binary_subtraction(num1, num2, bit_size=8):
    bin1 = decimal_to_binary_list(num1, bit_size)
    bin2_neg = Binary_negation(num2, bit_size)
    return add_bit_lists(bin1, bin2_neg)

def Binary_addtion(num1,num2,bit_size=8):
    bin1 = decimal_to_binary_list(num1)
    bin2 = decimal_to_binary_list(num2)
    return add_bit_lists(bin1,bin2)


print(Binary_subtraction(5, 3))
    

print(Binary_addtion(5,3))


