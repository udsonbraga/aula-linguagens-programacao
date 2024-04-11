nome_completo = input("nome e sobrenome: ")
nome, sobrenome = nome_completo.split()

nome = nome[0].lower() 
sobrenome = sobrenome[0].upper()

print(f"{nome}")
print(f"{sobrenome}")
