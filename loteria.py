import random

numeros_sorteados = []
numeros_jogados = []
lista_suporte = []
b = 0
a = 1
acertos = 0

while len(numeros_sorteados) != 6:
    numero_aleatorio = random.randint(1, 60)
    numeros_sorteados.append(numero_aleatorio)
    if numeros_sorteados.count(numero_aleatorio) > 1:
       numeros_sorteados.pop(numeros_sorteados.index(numero_aleatorio))


print('Esses foram os numeros sorteados: ', numeros_sorteados)


while len(numeros_jogados) != 6:
        numero_jogado = int(input(f'Digite o {a}º número que você deseja jogar'))
        numeros_jogados.append(numero_jogado)
        if numeros_jogados.count(numero_jogado) > 1:
            print('Número já adicionado')
            numeros_jogados.pop(numeros_jogados.index(numero_jogado))
            a -= 1
        a += 1

for numero in numeros_sorteados:
    lista_suporte.append(numero)

for numero in numeros_jogados:
    lista_suporte.append(numero)

for numero in range(0, len(lista_suporte)):
    if lista_suporte.count(lista_suporte[numero]) > 1:
        acertos += 1


print(lista_suporte)
print('Esses foram os numeros sorteados: ', numeros_sorteados)
print('Esses foram os numeros jogados: ', numeros_jogados)
print(acertos/2)


