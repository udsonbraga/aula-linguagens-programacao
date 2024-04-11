notas = []
nota = 0

while nota != -1:
    nota = float(input("nota (ou -1 para terminar): "))
    if nota != -1:
        notas.append(nota)

if len(notas) == 0:
    print("Nenhuma nota inserida.")
else:
    media = sum(notas) / len(notas)
   
    resultado = "Aprovado" if media >= 7 else "Reprovado"

    print(f"Média: {media}")
    print(resultado)
