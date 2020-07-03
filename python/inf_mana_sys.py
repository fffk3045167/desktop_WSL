#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from datetime import date

def menu():
    print("_" * 30)
    print("input 1 == add")
    print("input 2 == show")
    print("input 3 == out")
def add():
    print("input ex: school name age country")
    with open("information.txt", 'a') as f:
        f.write(input("input:"))
        f.write("  (")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        f.write(")")
        f.write('\n')
    print("add success!")

def show():
    with open("information.txt", 'r') as f:
        showinf = f.read()
        print(showinf)
    print("show information!")

while True:
    if __name__ == '__main__':
        menu()
        choice = int(input("sign in:"))
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            print("out !")
            break
