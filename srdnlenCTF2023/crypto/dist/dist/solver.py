from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def bytes_to_hex(byte_data): return ' '.join(f'{b:02x}' for b in byte_data)

with open("flag.enc", "rb") as f:
    c = f.readline()


#key = os.urandom(n)
#flag_enc = AES.new(key, AES.MODE_ECB).decrypt(c)

print(len(c))
print(c)
print(c[128:144])

