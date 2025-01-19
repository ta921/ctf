from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

cipherTexts = [
    '1ZjLniaqyx2UYUDThpSb5axNyFuBS4R/fmETSQiB22M=',
    'ourAlaqaIGQrlnyADJRgJ2b4+MXDjAWbudgLcsMz82I=',
    'kYN2b01rDE6lRHTSAoTQsnKpCL6wUB/UOgdvzJRqJmc=',
    '8t0VNpxXaT23s880C3cM+FUYH9/0hipXqlOlV4hluDU='
]

for cipherText in cipherTexts:
    print(cipherText.encode())
    plainText = b64decode(cipherText.encode())
    print(plainText)
    print(len(plainText))