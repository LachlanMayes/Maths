def get_parity_count(data_length):
    """Calculates how many parity bits are needed for data length."""
    # Formula: 2^parity_bit >= data_length + parity_bit + 1
    parity_bits = 0
    while (2**parity_bits < data_length + parity_bits + 1):
        parity_bits += 1
    return parity_bits

def hamming_encode(data):
    print(f"--- ENCODING DATA: {data} ---")
    data_length = len(data) #data length
    parity_bits = get_parity_count(data_length) # how many parity bits to add
    total_len = data_length + parity_bits # total length of data with parity bits
    
    # Create a list with '0' at index 0 (dummy) to make math 1-indexed like
    # We initialize everything to '0'
    code = ['0'] * (total_len + 1)
    
    # 1. Place Data Bits in non-power-of-2 positions
    # Powers of 2 are: 1, 2, 4, 8, 16...
    data_index = 0
    for i in range(1, total_len + 1):
        # Check if i is a power of 2 using bitwise math
        # If (i & (i-1)) == 0, it is a power of 2 (Parity spot)
        if (i & (i - 1)) != 0:
            code[i] = data[data_index]
            data_index += 1
            
    print(f"Bits placed (Parity empty): {''.join(code[1:])}")

    # 2. Calculate Parity Bits
    # Iterate through parity positions (1, 2, 4, 8...)
    for i in range(parity_bits):
        partiy_position = 2**i # The position of the parity bit (1, 2, 4...)
        
        # Check specific bits for this parity group
        # Logic: If bit position 'j' has a 1 at the 'p_pos' bit, check it.
        # Example: Parity 1 checks 1, 3, 5, 7...
        ones_count = 0
        for j in range(1, total_len + 1):
            if j & partiy_position: # If the bitwise AND is true, this position is covered
                if code[j] == '1':
                    ones_count += 1
        
        # Apply Even Parity Rule
        # If count is Odd, set parity bit to 1. If Even, set to 0.
        if ones_count % 2 != 0:
            code[partiy_position] = '1'
        else:
            code[partiy_position] = '0'
            
    encoded_str = "".join(code[1:])
    print(f"Final Encoded Hamming Code: {encoded_str}\n")
    return encoded_str

def hamming_correct(encoded_data):
    print(f"--- CHECKING RECEIVED: {encoded_data} ---")
    data_length_encoded = len(encoded_data)
    partiy_bits_count = 0
    # Figure out how many parity bits were in this string
    while (2**partiy_bits_count < data_length_encoded + 1):
        partiy_bits_count += 1
        
    # Convert string to list (1-indexed for easy math)
    code = ['0'] + list(encoded_data)
    
    error_pos = 0
    
    # Calculate Syndrome (Check Parity Bits)
    for i in range(partiy_bits_count):
        p_pos = 2**i
        ones_count = 0
        
        # Check the bits covered by this parity group
        for j in range(1, data_length_encoded + 1):
            if j & p_pos:
                if code[j] == '1':
                    ones_count += 1
        
        # If the count is Odd, there is an error in this group
        if ones_count % 2 != 0:
            print(f"Parity bit at pos {p_pos} detects an error.")
            error_pos += p_pos # Add the position value to find the error index
            
    if error_pos == 0:
        print("Result: No errors detected.")
        return encoded_data
    else:
        print(f"Result: ERROR DETECTED at position {error_pos}")
        
        # Flip the bit to fix it
        original_bit = code[error_pos]
        code[error_pos] = '0' if original_bit == '1' else '1'
        print(f"Fixing: Flipped bit {error_pos} from {original_bit} to {code[error_pos]}")
        
        corrected_str = "".join(code[1:])
        print(f"Corrected Code: {corrected_str}")
        return corrected_str

# --- MAIN EXECUTION ---

# 1. Encode the data
my_data = "1001101"
encoded = hamming_encode(my_data)

# 2. Simulate an Error
# Let's flip the bit at position 7 (Change '0' to '1')
# Note: String index is 6 because Python starts at 0
received_with_error = list(encoded)
received_with_error[6] = '1' if received_with_error[6] == '0' else '0'
received_with_error = "".join(received_with_error)

# 3. Detect and Correct
hamming_correct(received_with_error)


def calculate_hamming_distance(string1, string2):
    # The strings must be the same length
    if len(string1) != len(string2):
        return "Error: Strings must be the same length"
    
    distance = 0
    # Loop through every bit
    for i in range(len(string1)):
        # If they are different, add 1 to distance
        if string1[i] != string2[i]:
            distance += 1
            
    return distance

# Word 1: 10001001
# Word 2: 10110001
d = calculate_hamming_distance("10001001", "10110001")
print(f"Hamming Distance: {d}") 
# Output will be 3