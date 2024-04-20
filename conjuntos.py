conjunto_cores = {'vermelho', 'azul', 'amarelo', 'pretoebranco'}
# um conjunto é um SET
# o conjunto assim como o dicionário ele não é ordenado
#não consigo puxar dessa forma para pegar um conjunto especifico
#print(conjunto_cores[1])

conjunto_cores.add('vermelho')
conjunto_cores.add('azul')


conjunto_cores.remove('pretoebranco')
#vou utilizar um conjunto quando não quero coisas repetidas na lista
for cor in conjunto_cores:
    print(cor)