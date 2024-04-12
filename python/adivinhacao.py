import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    elif palpite < numero_secreto:
        print("O palpite é muito baixo.")
    else:
        print("O palpite é muito alto.")
    tentativas -= 1

if tentativas == 0:
    print("Você esgotou suas tentativas. O número secreto era:", numero_secreto)

print("Fim do jogo.")
