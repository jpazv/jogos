import random

numero = random.randrange(1, 1000)
tentativa = 1
lista = []
print('Tente adivinhar o número aleatório gerado pelo programa')
print('DICA: ele está no intervalo de 1-1000')
while numero != tentativa:
    print('-'*30)
    tentativa = int((input('Digite a sua tentativa: ')))
    print('-' * 30)
    if numero != tentativa:
        if tentativa > numero:
            print('O número {} é maior do que o número aleatório gerado'.format(tentativa))
            print('-' * 30)
            lista.append(1)
        if tentativa < numero:
            print('O número {} é menor do que o número aleatório gerado'.format(tentativa))
            print('-' * 30)
            lista.append(1)
    if numero == tentativa:
        print('Parabéns, você acertou!!!')
        print('Você necessitou de', sum(lista), ' tentativas para acertar')
        break

