"""
ARQUIVO EXTERNO DA REFERÊNCIA RÁPIDA.
constantes não existem no python
mas podemos nomear variáveis que
devem ser constantes com letras
maiusculas.
"""
PI = 3.14
OURO = 1.61



def bandeclay():
    print("bandeclay")
    return "bandeclay"


#Objeto abstrato e instância
#Classe e instância
class Pessoa:

    #método construtor __init__.
    def __init__(self, Nome, Idade, Peso):
        #self indica COISA DO OBJETO
        #sem self indica o parâmetro desta função construtora.
        self.nome = Nome
        self.idade = Idade
        self.peso = Peso
        self.email = 'name@domain' #valor default

    def info(self):
        print(self.nome, self.idade, self.peso)

    def envelhecer(self): 
        self.idade += 1

    def engordar(self, kilogramas):
        self.peso += kilogramas

    def emagrecer(self, kilogramas):
        self.peso -= kilogramas

    def adicionarEmail(self, correcao):
        self.email = correcao
        print(f'Email de {self.nome} foi alterado para {self.email}')

#Esta classe herda características
class Extraterrestre(Pessoa):
    pass

