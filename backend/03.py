#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

lista.sort()
print(lista)

#A função sort é nativa do python... mas não acho o jeito mais elegante de fazer isso. O bubble sort é uma forma boa de se fazer isso

#A melhor forma de resumir bubble sort é falando que ele sempre vai colocar o maior valor para o final da lista, assim criando uma lista crescente
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubbleSort(lista)
print(lista)