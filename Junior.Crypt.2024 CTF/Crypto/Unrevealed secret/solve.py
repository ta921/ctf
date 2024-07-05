import random

c = 'ﾚﾏﾒﾙﾓﾒﾆﾨﾉﾛￅﾢￎﾓﾞﾒﾙￌﾓﾚﾢﾛﾘ￉ﾉﾈﾏﾘ￈ﾢﾞ￉ﾓﾢﾏﾈￌﾓﾀ'
key = '������������������������������������������������������������'
#cBits =  [ord(i) for i in c]
#keyBits = [ord(i) for i in key]
#print(cBits)

def xor_cipher(message, key):
    # This function performs XOR encryption on the message and key
    message_nums = [ord(c) for c in message]
    key_nums = [ord(c) for c in key]
    cipher_nums = [m ^ k for m, k in zip(message_nums, key_nums)]
    return ''.join(chr(i) for i in cipher_nums)


if len(c) > len(key):
    raise ValueError("The key length must not be less than the message length")
if len(c) < len(key):
    key = key[:len(c)]

m = xor_cipher(c, key)
print(m) #grodno{Utf8_3ncod1ng_fe4ture5_c4n_ru1n}