import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = bytearray(random.randbytes(32))

data = bytearray(encoded_with_xor)

def xor_cipher(message, key):
    # This function performs XOR encryption on the message and key
    cipher_nums = [m ^ k for m, k in zip(message, key)]
    return ''.join(chr(i) for i in cipher_nums)

print(xor_cipher(data, key))
#LITCTF{sillyOTPlol!!!!sdfsgvkhf}
