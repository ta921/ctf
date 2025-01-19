from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

cipher = AES.new(key=b'aaaaaaaaaaaaaaaa', mode=AES.MODE_CBC)
plainText = "I am an authenticated admin, please give me the flag"
c = pad(b"I am an authenticated admin, please give me the flag", cipher.block_size)

cTob64 = b64encode(c)
print(c)
print(cTob64)
print(b64encode(b"I am an authenticated admin, please give me the flag"))
print(b64encode(b'm1z0r3_login_service: ID=admin'))

ans = \
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' +\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'