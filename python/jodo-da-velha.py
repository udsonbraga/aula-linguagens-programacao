def menu():
    print('__________________________\n')
    print("BEM VINDO AO JOGO DA VELHA!\n")
    print('__________________________\n')
    game()

def game():
    jogada = 0
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    while ganhou(board) == ' ':
        print("\nÉ a vez do jogador", 'X\n' if jogada % 2 == 0 else 'O')
        exibe(board)
        entrada = input("\nEm qual posição deseja jogar?: "'\n''>>:')
        posicoes = entrada.split()
        linha = int(posicoes[0])
        coluna = int(posicoes[1])

        if board[linha][coluna] == ' ':
            board[linha][coluna] = 'X' if jogada % 2 == 0 else 'O'
            escrever_tabuleiro(board)  # Escrever o estado atual do tabuleiro no arquivo 'tabuleiro.atual.txt'
        else:
            print("Posição inválida. Informe uma nova posição válida.")
            jogada -= 1

        jogada += 1

    #vencedor = ganhou(board)
    #if vencedor != 'Empate':
        #print("Jogador", vencedor, "ganhou após", jogada, "rodadas")
    #else:
        #print("O jogo terminou em empate.")

def ganhou(tabuleiro):
    # Checando linhas e colunas
    for i in range(3):
        if tabuleiro [i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]

    # Checando diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

    # Verificando se há empate
    for linha in tabuleiro:
        if ' ' in linha:
            return ' '
    return 'Empate'

def exibe(board):
    for i, linha in enumerate(board):
        print('|'.join(linha))  # Imprime as células de cada linha separadas por '|'
        if i < len(board) - 1:  # Verifica se não é a última linha do tabuleiro
            print('-' * 5)  # Imprime os traços separando as linhas

def escrever_tabuleiro(jogada):
    with open('tabuleiro.atual.txt', 'w') as arquivo:
        for linha in jogada[:-1]:  # Itera sobre todas as linhas, exceto a última
            arquivo.write('|'.join(linha) + '\n')
            arquivo.write('-'*5 + '\n')

        # Escreve a última linha sem adicionar os traços
        arquivo.write('|'.join(jogada[-1]) + '\n')


menu()
