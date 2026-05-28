""" Calculadora com while """

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite a operação desejada (+, -, *, /): ')
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except Exception as error:
        print(error)
    operadores = '+-*/'
    if operador in operadores:
        if operador == '+':
            print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
        elif operador == '-':
            print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
        elif operador == '*':
            print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')
        elif operador == '/':
            if num2_float != 0:
                print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
            else:
                print('Não é possível dividir por zero.')
    else:
        print('Operação inválida. Por favor, escolha entre +, -, *, /.')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break