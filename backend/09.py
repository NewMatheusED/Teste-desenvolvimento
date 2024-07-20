#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

import requests

#foi uma solução similar a anterior, minha ideia foi fazer um loop em cada usuário e fazer um append em uma nova lista apenas das informações que queremos, acho que é uma solução simples e eficiente
def getUsers():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    selectedUsers = []
    for user in users:
        selectedUsers.append({
            "nome": user["name"],
            "username": user["username"],
            "email": user["email"],
            "rua": user["address"]["street"],
            "numero": user["address"]["suite"]
        })
    print(selectedUsers)

getUsers()