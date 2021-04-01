#!/usr/bin/env python3
def main():
    num1 = promptNumber1()
    num2 = promptNumber2()
    print(promptOperation(num1,num2))
    
def promptNumber1():
    while True:
        try:
            num=input("First Number?")
            num=float(num)
        except:
            print("not a number")
        else:
            return num

def promptNumber2():
    while True:
        try:
            num=input("Second Number?")
            num=float(num)
        except:
            print("not a number")
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
            }
    while True:
        op=input("(A)dd, (S)ubtract, (D)ivide, (M)ultiply?").upper()
        if op in operations:
            if (op == "DIVIDE" or op=="D") and num2 == 0:
                return "DONT DESYTOY THE UNIVERSE!!\nNo Dividing By ZERO!!"
            return operations[op](num1,num2)
def updateTerminal():
    print("updateTerminal")
main()
