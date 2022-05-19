#este programa ajuda na coversão de bases.

#número  / base = proximo   resto
#proximo / base = proximo   resto2
#...
#ultimo / base = primeirodigito restoN

def main(base, modo):
    if modo == 1:
        numero = int(input("insira número: "))
        resto = 0
        for val in range(0,9):
            print("\n %s / %s = %s resto: %s"%(numero,base,numero/base,resto))
            resto = int(numero % base)
            numero = int(numero / base)
            if numero == 1:
                break
        return 1
    elif modo == 2:
        algarismo = int(input("insira um número maior que 1 para algarismo: "))
        numero = 0
        for posicao in range(0,algarismo):
            print("\n %s^%s = %s"%(base,posicao,base**posicao))
        return 1
    else:
        print("modo inválido")
        return 0

valor = int(input("insira a base: "))
print("\n1 Decimal para número em tal base.\n2 Para potencias de base")
modo =  int(input("insira o modo: "))
main(valor, modo)
