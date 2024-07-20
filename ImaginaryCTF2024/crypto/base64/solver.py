secret_key = [10, 52, 23, 14, 52, 16, 3, 14, 37, 37, 3, 25, 50, 32, 19, 14, 48, 32, 35, 13, 54, 12, 35, 12, 31, 29, 7, 29, 38, 61, 37, 27, 47, 5, 51, 28, 50, 13, 35, 29, 46, 1, 51, 24, 31, 21, 54, 28, 52, 8, 54, 30, 38, 17, 55, 24, 41, 1]
q = 64

j = 0
flag_int=0

for i in secret_key:
    flag_int += i*64**j
    j+=1

bit_len = flag_int.bit_length()
byte_len = (bit_len + 7) // 8
print(flag_int.to_bytes(byte_len, 'big'))
#b'ictf{b4se_c0nv3rs1on_ftw_236680982d9e8449}\n'
