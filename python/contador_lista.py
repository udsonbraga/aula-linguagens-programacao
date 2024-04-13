def contador(lista_de_palavras):
    qt_palavras = 0
    for palavra in lista_de_palavras:
        qt_palavras += 1
    print(f"Quantidade_palavras: {qt_palavras}")

    indice = 1
    for palavra in lista_de_palavras:
        qt_letras = 0
        for letra in palavra:
            qt_letras += 1
        print(f"Quantidade-palavras {indice}: {qt_letras}")
        indice += 1

lista_de_palavras = ["oi", "tubem", "palavra", "quadro"]

contador(lista_de_palavras)
