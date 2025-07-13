# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 1
# Requirement(s):
#
# Just a simple python calculator

import os

fnOperator = [" + ", " x ", " / ", " - "]

fnOperation = [lambda a, b: a + b,
               lambda a, b: a * b,
               lambda a, b: a / b,
               lambda a, b: a - b]

def main():
    os.system('cls')
    print(' *** Module 1 ***\n')

    try:
        while True:
            print("\n1-. Sum")
            print("2-. Multiply")
            print("3-. Divide")
            print("4-. Subtract")
            print("0-. Exit")
            x = int(input("\nYour choice: "))

            if x == 0:
                break
            elif 1 <= x < 5:
                index = x -1;
                op1 = float(input("First Operand: "))
                op2 = float(input("Second Operand: "))
                print(f"Result is {op1} {fnOperator[index]} {op2} = {fnOperation[index](op1, op2)}")

    except ValueError:
        print('Please enter a number\nExiting now...')

if __name__ ==  '__main__': main()