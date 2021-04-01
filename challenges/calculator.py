#!/usr/bin/env python3
def main():
    num1 = promptNumber("Input the First Number?")
    num2 = promptNumber("Input the Second Number?")
    print(promptOperation(num1,num2))
    
def promptNumber(string):
    while True:
        try:
            num=float(input(string))
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
            }
    while True:
        op=input("(A)dd, (S)ubtract, (D)ivide, (M)ultiply?").upper()
        if op in operations:
            if (op == "DIVIDE" or op=="D") and num2 == 0:
                return "DONT DESTROY THE UNIVERSE!!\nNo Dividing By ZERO!!"
            print()
            return operations[op](num1,num2)
        print(op,"not a valid operation. Try Add or Subtract")
def updateTerminal(num1='',num2='',op=''):

    
main()
