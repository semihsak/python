# Author: Semih SAK
# This script generate passwords how much you want and also you could save csv file.
# License MIT
# Usage: python random_pass_gen.py -c  "generated passwords show console output"
# Usage: python random_pass_gen.py -o  "generated passwords will store any csv file"

import csv
from sys import argv
from sys import exit
import random

filename = "pass.csv"
gpass = []

low="abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@!#/%^$&"

all = low + up + numbers + symbols

def writecsv():
    with open(filename,"w") as csvfile:
        writer = csv.writer(csvfile,delimiter='\n')
        writer.writerow(['passwords'])
        writer.writerow(gpass)

def passgen():
    for i in range(pieces):
        gpass.append("".join(random.sample(all,length)))

def compare():
    if length > 70 and pieces > 0:
        raise ValueError("Value for length is too large")
    
    elif length < 0 or pieces < 0:
        raise ValueError("Value length or pieces cannot be negative")
    
    elif length == 0 or pieces == 0:
        print("length or pieces cannot be zero")
        exit(1)

length = int(input("How much characters made your password : "))
pieces = int(input("How much times of password : "))

for arg in argv:
    
    if arg == "-o":
        compare()
        print(f"Generated passwords will store {filename} file")
        passgen()
        writecsv()
        print("Finished")
        
    elif arg == "-c": 
        compare()
        passgen()
        
        for x in gpass:
            print(x)

    elif len(argv) > 2:
        print("Too much arguments given")
        break