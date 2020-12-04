# Author: Semih SAK
# This script generate password how much you want.
# License MIT

from sys import exit
import random

gpass = []

low="abcdefghijklmnopqrstuvwxyz"
up = low.upper()
numbers = "0123456789"
symbols = "@!#/%^$&"

all = low + up + numbers + symbols

length = int(input("How much characters made your password : "))
pieces = int(input("How much times of password : "))

if length > 70 and pieces > 0:
    raise ValueError("Value for length is too large")
elif length < 0 or pieces < 0:
    raise ValueError("Value length or pieces cannot be negative")
elif length == 0 or pieces == 0:
    print("length or pieces cannot be zero")
    exit(1)

for i in range(pieces):
    gpass.append("".join(random.sample(all,length)))

for x in gpass:
    print(x)
