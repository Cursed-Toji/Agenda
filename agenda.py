AGENDA = {}
AGENDA['Victor'] = {
    'telefone': '0101010101',
    'email': 'victor@besteweb.com.br',
    'endereco': 'avenida brasil'
}

AGENDA['Cals'] = {
    'telefone': '02202544',
    'email': 'victor@besteweb.com.br',
    'endereco': 'avenida portugal'
}

def mostrar_contatos():

    # if len(AGENDA) > 0:
    if AGENDA:
        #vou definir todo o metodo aqui para depois chamar ele lá embaixo
        for contato in AGENDA:
            #pega o nome da pessoa da agenda
            # print("Nome: ", contato)
            #para imprimir os valores/infomraações que estão no contato fazer da forma abaixo
            #pega o conteudo do contato dentro da agenda
            # print("Telefone:",AGENDA[contato] ['telefone'])
            # print("E-mail:",AGENDA[contato] ['email'])
            # print("Endereço:",AGENDA[contato] ['endereco'])

            #todo Herdei o codigo do buscar
            buscar_contato(contato)
    else:
        print("agenda vazia, cadastre um contato para ver a agenda")



def buscar_contato(contato):
    try:
        print("Nome: ", contato)
        print("Telefone:",AGENDA[contato] ['telefone'])
        print("E-mail:",AGENDA[contato] ['email'])
        print("Endereco:",AGENDA[contato] ['endereco'])
        print('_______________________________________')
    except KeyError:
        print('Contato não localizado')
    except Exception as erro:
        print(erro)



def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco

def cadastrar_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()
    print()
    print('>>>> o Contato: {} foi adicionado/editado com sucesso'.format(contato))
    print()


def excluir_contato(contato):
    try:
    # o POP REMOVE O ITEM de dentro do json/dicionario
        AGENDA.pop(contato)
        salvar()
        print()
        print("Contato {} deletado com sucesso".format(contato))
    except KeyError: # se não localizar a chave que é o nome do contato entra aqui
        print("contato não encontrado")
    except Exception as error: # se der qualquer outro erro entra aqui
        print(error)




def menu():
    print('-----------')
    print('1 Mostrar todos os Contatos da agenda')
    print('2 Cadastrar  Contato')
    print('3 Excluir Contato')
    print('4 Buscar Contato ')
    print('5 Editar Contato ')
    print('6 Exportar contatos para CSV')
    print('7 Importar contatos por CSV ')
    print('0 Sair do Programa ')
    print('----------------------')


def optmenu():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    cadastrar_editar_contato(contato, telefone, email, endereco)


def exportar_contatos():
    try:
        with open('contato.csv', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato] ['telefone']
                email = AGENDA[contato] ['email']
                endereco = AGENDA[contato] ['endereco']
                # agenda.write(contato + telefone + email + endereco + '\n') dessa forma fica tudo junto
                arquivo.write('{};{};{};{}\n'.format(contato, telefone, email, endereco))

        print('Contato export com sucesso')
    except Exception as erro:
        print(erro)
        print("Algum erro ocorreu")


def importar_contato(nome_do_arquivo):
    try:
        #abrir no modo de leitura ==  modo R
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                #o strip vai remover o \n
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                cadastrar_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('arquivo não encontrado')
    except Exception as erro:
        print(erro)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        # abrir no modo de leitura ==  modo R
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # o strip vai remover o \n
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco
                }

    except FileNotFoundError:
        print('arquivo não encontrado')
    except Exception as erro:
        print(erro)


carregar()

while True:
    menu()
    opcao = input('Ecolher uma opção: ')
    if opcao == '1':
        mostrar_contatos()
############
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        if contato in AGENDA:
            print("------ Contato já existe ----")
        else:
            try:
                telefone, email, endereco = ler_detalhes_contato()
                cadastrar_editar_contato(contato, telefone, email, endereco)
            except Exception as e:
                print(f"Erro ao cadastrar o contato: {e}")


###################
    elif opcao == '5':
        contato = input('Digite o nome do contato a ser editado: ')

        if contato in AGENDA:
            telefone, email, endereco = ler_detalhes_contato()
            cadastrar_editar_contato(contato, telefone, email, endereco)
        else:
            print()
            print("Contato não encontrado.")
            print()


    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '0':
        print('Sair do Programa')
        break
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado:')
        importar_contato(nome_do_arquivo)
    else:
        print('Opção invalida')
