class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Divisão por zero não é permitida"
        else:
            return a / b

calc = Calculator()

while True:
    print("Escolha uma operação: \n 1- Adição \n 2- Subtração \n 3- Multiplicação \n 4- Divisão")

    operation = input("Digite a operação desejada (1/2/3/4): ")

    if operation == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(calc.add(num1, num2))

    elif operation == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(calc.subtract(num1, num2))

    elif operation == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(calc.multiply(num1, num2))

    elif operation == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(calc.divide(num1, num2))

    next_calculation = input("Deseja realizar outra operação? (s/n): ")
    if next_calculation == 'n':
        break