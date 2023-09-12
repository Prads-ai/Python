def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input('Enter first number : '))
    should_continue = True

    while should_continue:
        print('What operation do you want do ?: ')
        for symbol in operations:
            print(symbol)

        math_operator = input('pick an operator: ')

        num2 = int(input('Enter next number: '))
        calculate_function = operations.get(math_operator);
        result = calculate_function(num1, num2);

        print(f'{num1} {math_operator} {num2} = {result}')

        if input(f'type y to continue calculating with {result} or n to start a new calculation: ') == 'y':
            num1 = result
        else:
            calculator()


calculator()
