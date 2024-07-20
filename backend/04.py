#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

lista2 = []

#como todos os elementos da lista precisam passar por tratamento, a ideia foi fazer um loop e remover os espaços em branco com uma função nativa do python

for i in lista:
    lista2.append(i.strip())
print(lista2)