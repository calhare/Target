def inverte_string(string):
    invertida = ''
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

# Exemplo de uso
texto = "Hello, world!"
print(inverte_string(texto))
