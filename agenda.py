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
        print('_______________________________________')



def buscar_contato(contato):
    print("Nome: ", contato)
    print("Telefone:",AGENDA[contato] ['telefone'])
    print("E-mail:",AGENDA[contato] ['email'])
    print("Endereco:",AGENDA[contato] ['endereco'])



def cadastrar_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print('>>>> o Contato: {} foi adicionado/editado com sucesso'.format(contato))


def excluir_contato(contato):
    # o POP REMOVE O ITEM de dentro do json/dicionario
    AGENDA.pop(contato)
    print("Contato {} deletado com sucesso".format(contato))



def menu():
    print('1 Mostrar todos os Contatos da agenda')
    print('2 Cadastrar  Contato')
    print('3 Excluir Contato')
    print('4 Buscar Contato ')
    print('5 Editar Contato ')
    print('0 Sair do Programa ')
    opcao = input('Ecolher uma opção: ')
    try:

        if opcao == '1':
           mostrar_contatos()
        elif opcao == '2' or opcao == '5':
            contato = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o email do contato: ')
            endereco = input('Digite o endereco do contato: ')
            cadastrar_editar_contato(contato,telefone,email,endereco)
            mostrar_contatos(" o contato foi adicionado/editado {}".format(contato))

        elif opcao == '3':
            contato = input('Digite o nome do contato: ')
            excluir_contato(contato)
        elif opcao == '4':
            contato = input('Digite o nome do contato: ')
            buscar_contato(contato)
        elif opcao == '0':
         print('Sair do Programa')
        else:
            print('Opção invalida')


    except Exception as e:
        print('error', e)

menu()