while True:
    valor1 = int(input())
    
    if valor1 == -1:
        break
    
    operador = input()
    valor2 = int(input())
    
    resultado = 0
    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        resultado = valor1 / valor2
    else:
        print('Operador inválido')
    
    print(resultado)
