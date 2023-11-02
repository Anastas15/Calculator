from art import logo
print(logo(0))
def summ(num1, num2):
    summ = num1 + num2
    return summ

def substract(num1, num2):
    substract = num1 - num2
    return substract

def multiply(num1, num2):
    multiply = num1 * num2
    return multiply

def divide(num1, num2):
    divide = num1 / num2
    return divide


num1 = int(input('Write any number '))
num2 = int(input('Write any number '))

operations = {
    '+':summ, 
    '-':substract,
    '*':multiply,
    '/':divide
}


for key in operations:
    print(key)

symbol = input('Pick any symbol from above ')

calculation_function = operations[symbol]
first_answer = calculation_function(num1, num2)
print(f'{num1} {symbol} {num2} = {first_answer}')
stop = True
while stop:
    print(logo(first_answer))
    user_choise = input("Type 'y' to continue calculating with _ , or type 'n' to start a new calculation, or type 'quit' to exit calculator: ")
    if user_choise == 'y':
        stop = True
    if user_choise == 'n':
        stop = False
        break
    if user_choise == 'quit':
        stop = False
        break

    symbol = input('Pick any symbol from above ')
    calculation_function = operations[symbol]
    num = int(input('Write any number '))
    second_answer = calculation_function(first_answer, num)

    print(f'{first_answer} {symbol} {num} = {second_answer}')
    first_answer = second_answer