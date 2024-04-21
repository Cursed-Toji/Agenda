# arquivo = open('email.txt')
#
#
# conteudo = arquivo.readlines()
# conteudo_str = arquivo.read()
# print(conteudo)
#
# for linha in conteudo:
#     print(linha.strip()) #strip remove os espaços

try:
    arquivo = open('email.do')
except FileNotFoundError:
    print('arquivo não encontrado')
except Exception as erro:
    print(erro)
finally:
    try:
        arquivo.close()
    except Exception as erro:
        print(erro)

try:
    with open('email.txt') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('arquivo não encontrado')
except Exception as erro:
    print(erro)