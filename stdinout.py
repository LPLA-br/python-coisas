#argumentos de linha de comando com a linguagem
#python

import sys

#como é de conhecimento geral. O argumento 0 sempre será nome do programa
print("nome deste script é: ", sys.argv[0])

numero_de_argumentos = len(sys.argv)
print("total de argumentos passado para o programa: ", numero_de_argumentos)

if len(sys.argv) > 1:
    if sys.argv[1] == "args":
        for elemento in range(0, numero_de_argumentos):
            print(sys.argv[elemento], end = " ")
    else:
        if sys.argv[1] == "fale":
            print("\nfalei !")
