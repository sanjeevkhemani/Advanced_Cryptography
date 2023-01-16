from random import randint
import math

def Prime_Generator(R1, R2):
    x = randint(R1, R2)
    while True:
        if Primality_Test(x):
            break
        else:
            x += 1
    return x


def Primality_Test(x):
    i = 2
    root = math.ceil(math.sqrt(x))
    while i <= root:
        if x % i == 0:
            return False
        i += 1
    return True


def Modular_Inverse(a, m):
    g, x, y = Extended_GCD(a, m)
    if g != 1:
        return None
    else:
        return x % m


def Greatest_Common_Divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def Extended_GCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = Extended_GCD(b % a, a)
        return g, x - (b // a) * y, y


R1 = int(input("\nPlease enter the lower limit for the prime number range: "))
R2 = int(input("Please enter the upper limit for the prime number range: "))
p = Prime_Generator(R1, R2)
while True:
    q = Prime_Generator(R1, R2)
    if q != p:
        break

print("First Prime Number (p):\t\t", p)
print("Second Prime Number (q):\t", q)
modulus = p * q
φ = (p - 1) * (q - 1)
r = randint(2, 100)
while True:
    if Greatest_Common_Divisor(r, φ) == 1:
        break
    else:
        r += 1
public_exponent = r
print("Public Exponent (e):\t\t", public_exponent)
secret_exponent = Modular_Inverse(public_exponent, φ)
print("Secret Exponent (d)\t\t\t", secret_exponent)

print("\nEnter some plain text to encrypt: ")
plain_text = input()
print("Plain Text: \t\t\t\t", plain_text)
plain_text_ascii = [ord(x) for x in plain_text]
cipher_text = [(x ** public_exponent) % modulus for x in plain_text_ascii]
print("Cipher Text:\t\t\t\t", cipher_text)
decrypted_plain_ascii = [(x ** secret_exponent) % modulus for x in cipher_text]
decrypted_plain_text = [chr(x) for x in decrypted_plain_ascii]
print("Deciphered Plain Text: \t\t", decrypted_plain_text)
