""" REFERÊNCIA RÁPIDA PYTHON
Por: Luiz Paulo

ATENÇÂO
Este código, o módulo
e o __init__.py
devem estar dentro de
um diretório
chamado quickRef.

Experimente criar módulos externos .py
adicionando suas respectivas entradas
no arquivo __init__.py
----------------
diretório/
    __init__.py
    codigo1.py
    codigo2.py
    ...
    codigoN.py
----------------
"""

from refmodulo import PI, Pessoa, bandeclay

#from incluso import *
#Opcionalmente a declaração acima importa tudo do módulo.


"""
Jamais esquecerás do : (dois pontos)
no fim das seguintes declarações:
    condicionais
        if :
        elif :
        else :
    funções
        def a():
    classes
        class Carro:
"""

#Tipos de dados primitivos e operador de atribuição
#-------------------------------------------
verdadeiro, falso = True, False #atribuição múltipla
inteiro = 10
flutuante = 10.5
string = "referência rápida !"

stringMultilinha = """
Quae res in civitate duae plurimum possunt, eae contra nos ambae
faciunt in hoc tempore, summa gratia et eloquentia; quarum
alterum, C. Aquili, vereor, alteram metuo.
"""

#conversão de tipos
#-------------------------------------------

operacaoI   = int("10") + 10
operacaoII  = str(20) + " anos"
operacaoIII = float(5) / float(2)

#Entrada
#-------------------------------------------
entradaInteira = int(input("Insira um número "))
entrataTextual = input("Insira um Texto ")
entradaFlutuante = float(input("Insira um número flutuante "))

#Saída formatada
#-------------------------------------------
print("teste \"teste\" ")

print("teste", "teste2", 10, 2.5)

print("um inteiro " + str(inteiro) + " uma string: " + string)

print(f"{inteiro + 5}{flutuante + 6.78}")

print("um inteiro: %i e um string; %s flutuanteFormatado: %f" % (inteiro, string, 45.567564))
""" Descrição das letras prescedidas de % acima:
%s string
%i inteiro
%f flutuante
"""


#Dados compostos
#-------------------------------------------
"""
No rodapé deste código há links
que levam aos respectivos métodos
dos dados compostos abaixo
"""

lista = [1, "caros colegas", True, 4.67] #como um "array" do javascript

tupla = (1, "imutável", 2.5)    #como uma lista só que imutável

#como um "objeto" de javascript
dicionario = {
        "Idade":10,
        "nome":"Jerosveldson",
        "Peso":60,
        "coresFavoritas": ["azul","verde","laranja"]
}

print(dicionario["nome"])
print(dicionario["Idade"])
print(dicionario["coresFavoritas"][1])

#Operadores-----------------------------------

"""Operadores aritméticos
+   soma
-   subtração
*   multiplicação
/   divisão
%   resto de divisão
**  potência
//  divisão com resultado sem parte decimal
"""

"""Operadores lógicos:
 and
 or
 not

   Operadores de comparação são
   iguais aos de javascript
"""

#if elif else
#-------------------------------------------
"""
A construção switch case não existe no python.
"""

if inteiro == 0 or inteiro == 1:
    #declarações
    print("zero ou um")
elif inteiro == 2 and flutuante == 10.5:
    print("aaa")
else:
    print("bbb")

if True:
    if True:
        if True:
            print("true")
        elif False:
            print("etc.")
        else:
            print("false")
    else:
        print("false")
else:
    print("false")

if True:
    if True:
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            print("Hadouken !!! ==========>")

#Loops---------------------------------------
#i++ operador de incremento e decremento inexistente no python

lista2 = [1,2,3,4,5,6,7,8]

i = 0
while i <= 7:
    print(lista2[i])
    i += 1

print("--separador--")

for elemento in lista2:
    print(elemento)

print("--separador--")

for caractere in "rinoceteio0teste":
    print(caractere)
    if caractere == '0':
        break
    else:
        continue

print("--separador--")

for loopControlado in range(6):
    print(lista2[loopControlado])

print("--separador--")

for loopControlado in range(2,6):
    print(lista2[loopControlado])

print("--separador--")

#Funções--------------------------------------

def funcao(a, b, c):
    if a == b and a == c:
        print("a é igual b e c")
        return True
    else:
        print("a não é igual b e c")
        return False

a = funcao(1, 1, 1)
print(a)

#Módulo externo incluso.py--------------------------------
#como definido no arquivo __init__.py

#Instâncias da classe pessoa.
a1 = Pessoa("Ziraneida", 55, 98)
a2 = Pessoa("Marcolino", 92, 45)
a3 = Pessoa("Aldemar", 56, 102)

#Abaixo temos uma ação incorreta e não recomendada.
#esse atributo abaixo é único e existe apenas para Ziraneida
a1.codenome = "Ziraneida_Pimentinha"

#Email é um atributo que é inicializado com um valor padrão.
#Modifica-lo-emos adicionando os reais emails de Ziraneida, Marcolino e Aldemar.
a1.adicionarEmail("ZiraneidaPimentinha@gmail.com")
a2.adicionarEmail("MarcolinoCangaceiro@gmail.com")
a3.adicionarEmail("AldemarDasCachaças@gmail.com")

#chamando métodos que vão trabalhar com os atributos.
for i in range(6):
    a1.envelhecer()
    a1.engordar(2)
    a1.info()

print(PI)

BANDECLAY = bandeclay()
print(BANDECLAY)

""" Documentação na w3schools
PalavrasReservadasDaLinguagem: https://www.w3schools.com/python/python_ref_keywords.asp
Metodos:
    de String:      https://www.w3schools.com/python/python_ref_string.asp
    de Listas:      https://www.w3schools.com/python/python_ref_list.asp
    de tuplas:      https://www.w3schools.com/python/python_ref_tuple.asp
    de dicionários: https://www.w3schools.com/python/python_ref_dictionary.asp
    de funções embutidas: https://www.w3schools.com/python/python_ref_functions.asp
"""
