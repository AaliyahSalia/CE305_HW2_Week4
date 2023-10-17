def HamEncoding(msg):
    m = len(msg)
    k = 0
    while (2 ** k) < m + k + 1:
        k += 1
    encoded = ['0'] * (m + k)
    
    # Placing message bits at appropriate positions
    j = 0
    for i in range(1, m + k + 1):
        if i == 2 ** j:
            j += 1
        else:
            encoded[i-1] = msg[i-j-1]

    # Setting parity bits
    for i in range(k):
        pos = 2**i
        parity_bit_val = 0
        for j in range(1, len(encoded) + 1):
            if j & pos:
                parity_bit_val ^= int(encoded[j-1])
        encoded[pos-1] = str(parity_bit_val)

    print("k =", k)
    return ''.join(encoded)

def HamDecoding(rcv, k):
    n = len(rcv)
    error_pos = 0

    # Calculating error position
    for i in range(k):
        pos = 2**i
        parity_bit_val = 0
        for j in range(1, n + 1):
            if j & pos:
                parity_bit_val ^= int(rcv[j-1])
        error_pos += parity_bit_val * pos

    if error_pos == 0:
        print("No error")
    else:
        # Correcting the error
        rcv_list = list(rcv)
        rcv_list[error_pos - 1] = '1' if rcv[error_pos-1] == '0' else '0'
        print(f"Error at Position {error_pos}, and correct data: {''.join(rcv_list)}")

# Testing
org_sig1 = '1101'
print(HamEncoding(org_sig1))

org_sig2 = '1001011'
print(HamEncoding(org_sig2))

received_sig1 = '1010101'
HamDecoding(received_sig1, 3)

received_sig2 = '1010001'
HamDecoding(received_sig2, 3)

received_sig3 = '10110010011'
HamDecoding(received_sig3, 4)

received_sig4 = '10110000011'
HamDecoding(received_sig4, 4)