#!/usr/bin/env python3
######clear screen from chad
from subprocess import call
from os import name as osname
#####Chads Cool TRicks
import sys, time

def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

def clear(num1="",num2="",op="",result=""):
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')
    print("########################")
    if num1==op:
        print("###### CALCULATOR ######")
    else:
        print1by1(f"{num1} {op} {num2} = {result}\n")
    print("########################")
    print("########################")
    print("## 1 ##### 2 ###### 3 ##")
    print("########################")
    print("## 4 ##### 5 ###### 6 ##")
    print("########################")
    print("## 7 ##### 8 ###### 9 ##")
    print("########################")
    print("########## 0 ###########")
    print("########################")

def promptNumber(string):
    while True:
        try:
            num=input(string)
            num=float(num)
        except:
            print(num,"is not a valid number. Try Again!")
        else:
            return num

def promptOperation(num1,num2):
    operations= {
            "A": lambda a,b: a+b,
            "ADD": lambda a,b: a+b,
            "S": lambda a,b: a-b,
            "SUBTRACT": lambda a,b: a-b,
            "DIVIDE": lambda a,b: a/b,
            "D": lambda a,b: a/b,
            "M": lambda a,b: a*b,
            "Multiply": lambda a,b: a*b,
            "op":{
                "A":"+",
                "S":"-",
                "M":"*",
                "D":"/",
                }
            }
    while True:
        op=input("(A)dd, (S)ubtract, (D)ivide, (M)ultiply?").upper()
        if op in operations:
            if (op == "DIVIDE" or op=="D") and num2 == 0:
                return ["\nDONT DESTROY THE UNIVERSE!!\nNo Dividing By ZERO!!","/"]
            return [operations[op](num1,num2),operations["op"][op[0]]]
        print(op,"not a valid operation. Try Add or Subtract")

def main():
    while True:
        clear()
        num1 = promptNumber("Input the First Number?")
        clear(num1)
        num2 = promptNumber("Input the Second Number?")
        clear(num1,num2)
        answer = promptOperation(num1,num2)
        clear(num1,num2,answer[1],answer[0])
        state = input("Stop Calculating? \n(Y)/(N)?\n").upper()
        if state == "Y":
            print1by1("Thank you for using my Calculator\n")
            break
if __name__ == "__main__":
    main()
