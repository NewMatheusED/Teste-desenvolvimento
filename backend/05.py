#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]
lista2 = []

#primeiro adiriono o segundo item da lista em outra, a fim de guardar a informação, depois removo o item da primeira lista, tudo isso usando como base seu valor de index, sendo o segundo item, seu index é 1
lista2.append(lista[1])
lista.pop(1)
print(lista2)