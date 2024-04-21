def divisao(n1,n2):
    try: # se vai dar certo entra aqui
        print(n1/n2)
    except Exception as error:# se ele verificar que vai dar erro entra aqui
       #quanto usa  except Exception, qualquer exceção que der aqui vai entrar no erro
        print("divisão invalida")
        print(error)
try:
    a1 = float(input('Digite um numero 1: ')) #ValueError
    b2 = float(input('Digite um numero 2: '))
    print(a1/b2) #ZeroDivisionError
except ValueError as error: # tratando strings
    print("Digite apenas numeros")
except ZeroDivisionError as error: # tratando divisão por 0
    print("não pode dividir por zero")
except Exception as error:
    print(error)
finally:
    print('Fim do programa')