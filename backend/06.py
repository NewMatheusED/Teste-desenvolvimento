#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#faço um loop na lista, mas em vez de fazer i in lista, faço no tamanho da lista, a fim de ter como valor do loop o index da lista, assim consigo comparar e alterar o valor mais facilmente
for i in range(len(lista)):
    if lista[i] == "joao":
        lista[i] = "maria"

print(lista)