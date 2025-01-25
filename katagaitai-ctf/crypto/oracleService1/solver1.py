from pwn import *
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import isPrime
import math

m = int(b'katagaitai-CTF'.hex(),16)

m1 = 2069005277
m2 = m // m1

print(m)

print(format(m1, 'x'))
print(format(m2, 'x'))

print(len(format(m1, 'x')))
print(len(format(m2, 'x')))
print(long_to_bytes(m1 * m2))