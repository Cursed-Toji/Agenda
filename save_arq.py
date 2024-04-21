try:
   # with open('arq.txt', 'a') as arquivo:  modo append vai adicojanr mais coisas ao arquivo
   # o modo a vai ler o arquivo que existe e depois vai adicionar o texto ao  arquivo

    # usar o modo W faz criar um arquivo em branco     with open('arq.txt', 'w') as arquivo:
    with open('arq.txt', 'a') as arquivo:
        #o arquivo.write é para escrever dentro do arquivo
        arquivo.write('Joao beste\n')
except Exception as erro:
    print(erro)

'''
 Modo - 'r' Abre para ler
 Modo - 'w' Abre para escrever/ o arquivo é sobrescrito
 Modo - 'a' Abre para escrever/ novo conteudo e add ao final do arquivo
'''