resultado =' o jogo não acabou'

with open ('jogo_tabuleiro.txt', 'r') as arquivo:
    # aqui ocorre a leitura de todas as linhas e armazena na variável 'linhas'
    linhas = arquivo.readlines()
    #aqui verifico as linhas 0,2,4 , removo as quebras de linha com 'strip' e divido os elemontos com 'split'.
    tabuleiro =   [linhas [0].strip('\n').split('|'), 
                   linhas [2].strip('\n').split('|'), 
                   linhas [4].strip('\n').split('|')]
    #verificação se não há espaços vazios
    for linha in tabuleiro:
        for jogada in linha:
            if jogada == ' ':
                resultado = 'o jogo não acabou'
    
    for linha in tabuleiro:
        if linha [0] == linha [1] == linha [2] and linha [0] != ' ':
            resultado = linha [0]
                
    for coluna in [0,1,2]:
        if tabuleiro [0][coluna] == tabuleiro [1][coluna] == tabuleiro [2][coluna] and tabuleiro [0] != ' ':
            resultado = linha [0][coluna]
            
    if (tabuleiro [0][0] == tabuleiro [1][1] == tabuleiro [2][2] == tabuleiro):
        resultado = tabuleiro[1][1]
        
    if resultado == ' ':
        resultado = 'empate'
                
    print(resultado)