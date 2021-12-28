# from art import logo
# print(logo)
logo = """
 _____________________
|  _________________  |
| | Simple Calc     | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    should_end = False
    num1 = float(input("Masukkan angka pertama: "))
# function = input("Masukkan operasi yang anda inginkan: ")
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Masukkan operasi yang ingin anda lakukan: ")
# num2 = int(input("Masukkan angka kedua: "))

# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")

    while not should_end:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Masukkan operasi yang ingin anda lakukan: ")
        num2 = float(input("Masukkan angka kedua: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        end = input(
            'Masukkan "y" untuk melanjutkan, masukkan "a" untuk memulai dari awal, masukkan "n" untuk berhenti: ')
        if end == "y":
            num1 = answer
        elif end == "a":
            calculate()
        elif end == "n":
            should_end = True


calculate()
