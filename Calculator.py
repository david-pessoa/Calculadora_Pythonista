import math
from logo import logo
operations1 = ["sqrt","!"]
operations2 = ["+","-","*","/","//","%","**","log"]
specials = ["M","M+", "CE"]
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2
def divide_trunc(n1,n2):
    return n1//n2
def mod(n1,n2):
    return n1 % n2
def power(n1, n2):
    return n1 ** n2
def square_rt(n1):
    return math.sqrt(n1)
def fatorial(n1):
    tipo = str(type(n1))
    if tipo != "<class 'int'>":
        print("You typed an invalid number")
    else:
        return math.factorial(n1)
def logaritmo(n1, n2):
    return math.log(n1,n2)
memory = 0
def start():
    print(logo)
    for i in ["+","-","*","/","//","%","**","log","sqrt","!","M","M+", "CE"]:
        print(i)
    first = float(input("Choose the first number:"))
    return first
num1 = start()
num =  num1
while True:
    operacao = input("Choose an operation: ")
    while (operacao not in operations1) and (operacao not in operations2) and (operacao not in specials):
        print("Invalid operation")
        operacao = input("Choose an operation: ") 
    if operacao in specials:
        if operacao == specials[0]:
            resp = memory
        elif operacao == specials[1]:
            memory = resp
        else:
            resp = 0
        print(resp)
    else:
        if operacao in operations1:
            if operacao == operations1[0]:
                resp = square_rt(num)
            elif operacao == operations1[1]:
                resp = fatorial(num)
            print(f"{num} {operacao} = {resp}")            
        else:
            num2 = float(input("Choose the next number: "))
            if operacao == operations2[0]:
                resp = add(num1,num2)
            elif operacao == operations2[1]:
                resp = subtract(num1,num2)
            elif operacao == operations2[2]:
                resp = multiply(num1,num2)
            elif operacao == operations2[3]:
                resp = divide(num1,num2)
            elif operacao == operations2[4]:
                resp = divide_trunc(num1,num2)
            elif operacao == operations2[5]:
                resp = mod(num1,num2)
            elif operacao == operations2[6]:
                resp = power(num1,num2)
            elif operacao == operations2[7]:
                resp = logaritmo(num1,num2)
            print(f"{num1} {operacao} {num2} = {resp}")
    answer = input(f"Do you want to continue calculating with: {resp}, reset de calculator or exit? Type 'continue', 'reset' or 'exit'.").lower()
    print("\n")
    if answer == "exit":
        break
    elif answer == 'reset':
        num1 = start()
        num =  num1 
    else:
        num = resp
        num1 = resp