
#o dicionario tem chave e valor
dicionario = {
    "tijolo" : "objeto para montar uma casa",
    "Massa" : "cimenta para uma casa",
}
dicionario_aluno = {
    "victor" : "tem 19 ano",
    "maria" : "tem 17 anos",
    "diego" : "tem 15 anos",
    "lucas" : "tem 15 anos",
    "joão" : 20,
    "gabi" : 21
    #gabi é a chave : 21 é o valor
    # 1 vem a chave depois dos dois pontos : vem o valor
}

# no dicionario não posso trazer os itens pelo [0], tenho que trazer a chave que seria o tijolo
print(dicionario['tijolo'])
print(dicionario['Massa'])
print(dicionario['tijolo'])

print(dicionario_aluno)
print(dicionario_aluno['victor'])

# para cada pessoa que está em dicionario aluno vai me mostrar na tela
for pessoas in dicionario_aluno:
    print(pessoas)


#se eu quiser só as idades preciso puxar o valor então
for pessoas in dicionario_aluno.values():
    print(pessoas)

#Desta forma puxo só as chaves que são as pessoas
for pessoas in dicionario_aluno.keys():
    print(pessoas)

 