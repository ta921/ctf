from itertools import cycle

flag = b"uiuctf{hgfedcbahgfedcbahgfedcbahgfedcbahgfedcba}"
# len(flag) = 48
key  = b"abcdefgh"
# len(key) = 8
ct = bytes(x ^ y for x, y in zip(flag, cycle(key)))
print(ct)
print(flag[0],key[0])
print((flag[0] ^ key[0]))

#with open("ct", "wb") as ct_file:
#   ct_file.write(ct)
