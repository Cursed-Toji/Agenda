#essa agenda vai ser um dicinario

agenda = {
    "victor" : "9999-9999",
    "death" : "9999-8888",
    "dcals" : "9999-9919",
    "cals" : "9999-9998",
    "joao" : "9999-9977",
}

agenda_completa = {
    "gabriel":{
        "telefone" : "9999-1010",
        "e-mail" : "contato@besteweb.com.br",
        "endereco" : "avenida parana"
    },
    "gabizinha": {
        "telefone": "9920-1010",
        "e-mail": "contato33@besteweb.com.br",
        "endereco": "avenida brasil"
    },
    "vitinho": {
        "telefone": "9220-1010",
        "e-mail": "contato3366@besteweb.com.br",
        "endereco": "avenida portugal"
    }
}


#mudar o dado de alguem
agenda_completa ['vitinho'] ['e-mail'] = "vitin@besteweb.com.br"

agenda_completa  ['luqueta'] = {
    'telefone' : '9911-1010',
    'e-mail' : 'lucas@besteweb.com.br',
    'endereco' : 'avenida besteweb'
}

#trazer o numero da maria
print(agenda['cals'])
#pego todos os dados do gabriel
print(agenda_completa['gabriel'])

#pegar um dado só do vitinho
print(agenda_completa['vitinho'] ['e-mail'])

print(agenda_completa['luqueta'] ['e-mail'])

for contato in agenda_completa:
    print(contato)

agenda_completa.pop('vitinho')

print(agenda_completa)
