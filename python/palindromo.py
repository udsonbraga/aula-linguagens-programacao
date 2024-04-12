texto = input("Digite um texto: ")

# Remover espaços e pontuações, e converter para minúsculas
texto = texto.lower()
texto = ''.join(e for e in texto if e.isalnum())

# Inverter o texto
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
