#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

import requests

def getTasks():
    #faço a request
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    #transformo a request em json pra melhorar a leitura e manipulação 
    tasks = response.json()
    completed = 0
    pending = 0
    #faço um loop em cada task, já que a chave completed está no mesmo nível de todas as outras chaves, fica mais simples o loop assim
    for task in tasks:
        #como a chave completed usa valor booleano, fazer a verificação de forma direta resolve o problema com mais facilidade
        if task["completed"]:
            completed += 1
        else:
            pending += 1
    #faço um print de saída mais completo, deixando claro quais tasks foram concluidas ou não, usando concatenação f string
    print(f"Concluidas: {completed} \nPendentes: {pending}")

print(getTasks())
