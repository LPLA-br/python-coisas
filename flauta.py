#simples programa agilizar cálculo de porcentagem.
#na confecção de flautas pvc

distanciaTotal = int(input("insira o tamanho total do furo até o fim da flauta: "))

#resolve coisa como 50% de N centimetros
def porcentagem(porcentoDoTotal):
    return (distanciaTotal*porcentoDoTotal) / 100

a = 5
#posição a N% de distância do furo de sopro.
valores = [43, 50, 58, 68, 73, 83]
while a != -1:
    print( porcentagem( valores[a] ) )
    a -= 1
