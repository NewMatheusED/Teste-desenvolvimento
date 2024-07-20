#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta


#minha ideia foi criar duas classes, uma para gerenciar as ações da conta individual, outra para gerenciar ações que normalmente o banco toma, como identificação, depósitos e saques. Seria possível fazer tudo só com a classe Conta, mas queria algo mais dinâmico e que pode ser expandido caso necessário. Imagino que a divisão de classes seja mais simples de entender e manter.
class Conta:
    def __init__(self, nome, cpf):
        self.id = 0
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if(valor > self.saldo):
            print(f"Saldo insuficiente para saque de {valor} na conta de {self.nome}")
            return
        else:
            self.saldo -= valor

    def panorama(self):
        print(f"ID: {self.id} \nNome: {self.nome}\nCPF: {self.cpf}\nSaldo: {self.saldo} \n--------------------------------------------------------------------------")

class InterfaceBanco:
    def __init__(self):
        self.contas = []
        self.id = 0

    def criarConta(self, nome, cpf):
        conta = Conta(nome, cpf)
        conta.id = self.id
        self.contas.append(conta)
        self.id += 1
        return conta

    #a ideia de 'recriar' os métodos de deposito e saque aqui foi para ser mais fácil identificar para qual conta você quer depositar, já que todas as contas vão estar armazenadas em um array nessa classe
    def deposito(self, id, valor):
        for conta in self.contas:
            if conta.id == id:
                conta.deposito(valor)
                return conta

    def saque(self, id, valor):
        for conta in self.contas:
            if conta.id == id:
                conta.saque(valor)
                return conta
    
    #apenas um método para analisar as contas e ver se está tudo certinho
    def mostrarContas(self):
        for conta in self.contas:
            conta.panorama()
            

banco = InterfaceBanco()
conta1 = banco.criarConta("João", "123.456.789-00")
conta2 = banco.criarConta("Maria", "987.654.321-00")
conta3 = banco.criarConta("José", "321.654.987-00")
banco.deposito(conta1.id, 1000)
banco.saque(conta2.id, 100)
banco.mostrarContas()
