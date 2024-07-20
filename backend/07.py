#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0

#não tem muito o que explicar na realidade, não há outra solução pra isso imagino, como o pedido foi bem específico para loop while, imagino que seja a única solução 
while i <= 5:
    print(lista[i])
    i += 1
