# Calculadora em Python


def input_numbers():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    return x, y


print('******************** Python Calculator ***********************')

print('Selecione o número da operação desejada:')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

op = int(input('Digite sua opção (1/2/3/4): '))

if op == 1:
    x, y = input_numbers()
    print('%d + %d = %d' % (x, y, x + y))

elif op == 2:
    x, y = input_numbers()
    print('%d - %d = %d' % (x, y, x - y))

elif op == 3:
    x, y = input_numbers()
    print('%d * %d = %d' % (x, y, x * y))

elif op == 4:
    x, y = input_numbers()
    print('%d / %d = %f' % (x, y, x / y))

else:
    print('Opção inválida!')
