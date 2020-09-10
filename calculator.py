def check_isdigit(n):
    f = 1
    try:
        float(n)
    except ValueError:
        f = 0
    while f == 0:
        n = input("Not a number. Enter a number: ")
        try:
            float(n)
            f = 1
        except ValueError:
            f = 0
    return float(n)

fin = ''
th = {'/', '*', '-', '+'}

while fin != '!':
    a = input("Enter a number: ")
    a = check_isdigit(a)

    b = input("Enter an operand: ")
    while b not in th:
        b = input("Choose operand from /, *, -, + and write it")

    c = input("Enter a number: ")
    c = check_isdigit(c)

    if b == "+": print(a+c)
    elif b == "-": print(a-c)
    elif b == "/": print(a/c)
    else: print(a*c)

    print("Enter ! to finish or any key to continue")
    fin = input()


