# Author: Semih SAK
# This script generate password how much you want.
# License MIT

import random

gpass = []

low="abcdefghijklmnopqrstuvwxyz"
up = low.upper()
numbers = "0123456789"
symbols = "@!#/%^$&"

all = low + up + numbers + symbols

length = int(input("How much characters made your password : "))
pieces = int(input("How much times of password : "))

for i in range(pieces):
    gpass.append("".join(random.sample(all,length)))

for x in gpass:
    print(x)
