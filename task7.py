def calculator(a,b,c):
    if c == "a":
        d = a+b
        print(a,"+",b,"=",d)
    elif c == "b":
        d = a-b
        print(a,"-",b,"=",d)
    elif c == "c":
        d = a/b
        print(a,"/",b,"=",d)
    elif c == "d":
        d = a*b
        print(a,"*",b,"=",d)
    elif c == "e":
        d = a**b
        print(a,"**",b,"=",d)
    else:
        print("invalid input")

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
print('Enter:\n"a" if you want to add\n"b" if you want to subtract\n"c"if you want to divide \n"d" if you want to do multiplication \n"e" if you want to square a number')
choice = input("Enter your choice: ")

calculator(number1,number2,choice)