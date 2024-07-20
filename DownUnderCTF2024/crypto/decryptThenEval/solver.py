#!/usr/bin/env python3
import socket
from Crypto.Util.strxor import strxor

def recvuntil(s, tail):
    data = b''
    while True:
        if tail in data:
            return data.decode()
        data += s.recv(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('2024.ductf.dev', 30020))

xor_key = b''
for i in range(4):
    for j in range(256):
        ct = strxor(xor_key, b'1' * i) + bytes([j])
        ct_hex = ct.hex()
        data = recvuntil(s, b': ')
        print(data + ct_hex)
        s.sendall(ct_hex.encode() + b'\n')
        data = recvuntil(s, b'\n').rstrip()
        print(data)
        if data == '1' * (i + 1):
            xor_key += bytes([j ^ ord('1')])
            break

ct = strxor(xor_key, b'FLAG')
ct_hex = ct.hex()
data = recvuntil(s, b': ')
print(data + ct_hex)
s.sendall(ct_hex.encode() + b'\n')
data = recvuntil(s, b'\n').rstrip()
print(data)