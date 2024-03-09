def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        print(f'O número {numero} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')

# Exemplo de uso
verifica_fibonacci(21)
