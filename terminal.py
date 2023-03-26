import os
import sys
import datetime as dt
import subprocess
import math as mth
while True:
    userinput = input("enter a command --> ")

    if userinput == "help":
        print("commands: createfile, writefile, deletefile, breakwrite, exit, whichos, time, addition, subtraction, multiply, divide, pythagoreas, exponent, squareroot")
    elif userinput == "createfile":
        filename = input("enter filename (include extension): ")
        f = open(filename, "a")
    elif userinput == "writefile":
      content = input("enter text to write: ") 
      while content != "exit":
        try:    
            f.write(content + "\n")
            content = input("enter more text to write: ") 
        except:
            print("you can't write to a file after write is broken/if you never created one silly")
    elif userinput == "breakwrite":
        f.close()
        print("file closed, write operations no longer usable")
    elif userinput == "exit":
        break
    elif userinput == "whichos":
        print(sys.platform)
    elif userinput == "time":
        print(dt.datetime.now())
    elif userinput == "readfile":
        try:
            filenametoread = input("which file to read? (include the extension): ")
            file1 = open(filenametoread, "r")
            print(file1.read())
        except:
            print("cannot read file that does not exist/write not broken")
    elif userinput == "deletefile":
        try:    
            deletefilename = input("enter file name (include extension): ")
            os.remove(deletefilename)
            print("file be gone")
        except:
            print("file does not exist/deletion error")
    elif userinput == "addition":
        try:
            add1 = int(input("enter first number: "))
            add2 = int(input("enter second number: "))
            sum = add1 + add2
            print(sum)
        except:
            print("enter a NUMBER")
    elif userinput == "subtraction":
        try:
            sub1 = int(input("enter first number: "))
            sub2 = int(input("enter second number: "))
            diff = sub1-sub2
            print(diff)
        except:
            print("enter a number")
    elif userinput == "multiply":
        try:
            mult1 = int(input("enter first number: "))
            mult2 = int(input("enter second number: "))
            end = mult1*mult2
            print(end)
        except:
            print("enter a NUMBER")
    elif userinput == "divide":
        try:    
            div1 = int(input("enter first number: "))
            div2 = int(input("enter second number: "))
            dividend = div1/div2
            print(float(dividend))
        except:
            print("enter a NUMBER")
    elif userinput == "pythagoreas":
        try:
            leg1 = int(input("enter leg 1: "))
            leg2 = int(input("enter leg 2: "))
            leg3 = mth.sqrt((leg1*leg1) + (leg2*leg2))
            print(float(leg3))
        except:
            print("enter a NUMBER")
    elif userinput == "exponent":
        try:
            base = int(input("enter base: "))
            exponent = int(input("enter exponent: "))
            equals = base**exponent
            print(float(equals))
        except:
            print("enter a NUMBER")
    elif userinput == "squareroot":
        try:
            besqrt = int(input("what do you want the root of?: "))
            root = mth.sqrt(besqrt)
            print(float(root))
        except:
            print("enter a number/positive number")

    else:
        print(userinput + " isn't a command")
