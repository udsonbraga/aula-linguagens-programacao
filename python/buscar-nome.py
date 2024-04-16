from datetime import datetime

busca = input('Qual nome você busca: ')
busca_nome, busca_sobrenome = busca.split(' ')
busca_nome = busca_nome.lower()
busca_sobrenome = busca_sobrenome.lower()

with open('alunos.cvs','r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()
    
    for linha in lista_linhas:
        nome_chamada, data_nascimento, matricula = linha.strip('\n').split(',')
        nome, sobrenome, numero = nome_chamada.split(' ')
        
        if (nome.lower () == busca_nome and sobrenome.lower() == busca_sobrenome):
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%y')
        
        hoje = datetime.now()
        idade = hoje.year - data_nascimento.year
        print('NOME>', nome_chamada,'IDADE>', idade)
