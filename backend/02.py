#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

#faço um loop em todos os produtos
for produto in responsejson['produtos']:
    #caso o produto seja o desejado, mostra o valor dele
    if produto['nome'] == 'Produto B':
        print(produto['preço'])
        #a fim de economizar memória e evitar loop desnecessário (pensando que só há 1 produto com o nome), paramos o loop com o break
        break