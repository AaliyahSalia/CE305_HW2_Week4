def binary_long_division(dividend, divisor):
    n = len(divisor)
    #Append zeroes to the divident
    dividend += '0' * (n-1)
    for i in range(len(dividend)-n+1):
        if dividend[i] == '1':
            for j in range(n):
                #XOR operation
                dividend = dividend[:i+j] + str(int(dividend[i+j]) ^ int(divisor[j])) + dividend[i+j+1:]
    return dividend[-(n-1):]

def encoding(msg, poly):
    remainder = binary_long_division(msg, poly)
    return msg + " " + remainder

def decoding(rcv, poly):
    remainder = binary_long_division(rcv.replace(" ", ""), poly)
    if '1' in remainder:
        return 'Error'
    else:
        return 'No Error'

#Test Cases
org_sig1 = '1010'
poly = '100101'
print(encoding(org_sig1, poly))

org_sig2 = '1100'
poly = '100101'
print(encoding(org_sig2, poly))

received_sig1 = '1010 00111'
print(decoding(received_sig1, poly))

received_sig2 = '1010 01111'
print(decoding(received_sig2, poly))

received_sig3 = '1100 11001'
print(decoding(received_sig3, poly))

received_sig4 = '1100 11111'
print(decoding(received_sig4, poly))
