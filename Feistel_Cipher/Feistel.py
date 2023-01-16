import binascii

print("\nEnter some plain text to encrypt: ")
plain_text = input()
print("Plain Text: \t\t\t", plain_text)

plain_text_ascii = [ord(x) for x in plain_text]
plain_text_binary = [format(y, '08b') for y in plain_text_ascii]
plain_text_binary = "".join(plain_text_binary)

n = int(len(plain_text_binary) // 2)
L0 = plain_text_binary[0:n]
R0 = plain_text_binary[n::]
key_length = len(R0)

def key_gen(p):
    import random
    key = ""
    p = int(p)
    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key = key + temp
    return (key)

def ex_or(a, b):
    temp = ""
    for i in range(n):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
    return temp

K = key_gen(key_length)
#print("R0: ", R0)
#print("L0: ", L0)
#print("K:  ", K)
K = int(K, 2)
for e in R0:
    e = int(e, 2)
    e = pow(e, K)
    e = 2*e % 16
f1 = R0
R1 = ex_or(f1, L0)
L1 = R0

bin_data = L1 + R1
str_data = ' '

for i in range(0, len(bin_data), 7):
    temp_data = bin_data[i:i + 7]
    decimal_data = int(temp_data, 2)
    str_data = str_data + chr(decimal_data)

print("Cipher Text:\t\t\t", str_data)

L2 = L1
R2 = R1

for e in L2:
    e = int(e, 2)
    e = pow(e, K)
    e = 2*e % 16
f2 = L2
L3 = ex_or(R2, f2)
R3 = L2
decrypted_plain_text = L3 + R3

decrypted_plain_text = int(decrypted_plain_text, 2)
decrypted_plain_text = binascii.unhexlify('%x' % decrypted_plain_text)
decrypted_plain_text = decrypted_plain_text.decode('ascii')
print("Deciphered Plain Text: \t", str(decrypted_plain_text))