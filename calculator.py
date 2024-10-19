import os
def fun(n1,operator,n2):
    match operator:
        case '+':
            return n1+n2
        case '-':
            return n1-n2
        case '*':
            return n1*n2
        case '/':
            return n1/n2


def calculator():
    n1=int(input())
    flag=True
    while flag:
        operator=input()
        n2=int(input())
        c=fun(n1,operator,n2)
        print(c)
        new=input(f"enter 'c' to continue operation with{c}\nenter 'Q' to quit\nenter 'n' to perform new operation").lower()
        if new=='c':
            n1=c
        elif new=='n':
            flag=False
            os.system('cls')
            c=calculator()
        elif new=='q':
            return c
    return c
c=calculator()
print(f"the output is: {c}")