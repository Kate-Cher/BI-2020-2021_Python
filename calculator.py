def check_isdigit(num):
    fl = 1
    try:
        float(num)
    except ValueError:
        fl = 0
    while fl == 0:
        num = input("Not a number. Enter a number: ")
        try:
            float(num)
            fl = 1
        except ValueError:
            fl = 0
    return float(num)


print("List of valid operators:" + '\n' +
      "Use * for multiplication" + '\n' +
      "Use / for division" + '\n' +
      "Use + for addition" + '\n' +
      "Use - for subtraction" + '\n' +
      "Use ** for exponentiation" + '\n' +
      "Use // for floor division" + '\n' +
      "Use % for modulus operator" + '\n')
final = ''
operators_list = {'/', '*', '-', '+', '%', '**', '//'}

# Checking for more then one operation
while final != '!':

    # Getting numbers and operator from user
    num1 = input("Enter a number: ")
    num1 = check_isdigit(num1)

    operator = input("Enter an operator: ")
    while operator not in operators_list:
        operator = input("Your operator isn't valid.\n
                         Choose operator from list above and write it: ")

    num2 = input("Enter a number: ")
    num2 = check_isdigit(num2)

    # Calculations
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "**":
        print(num1**num2)
    elif operator == "//":
        print(num1 // num2)
    elif operator == "%":
        print(num1 % num2)

    print("Enter ! to finish or any key to make more calculations")
    final = input()
