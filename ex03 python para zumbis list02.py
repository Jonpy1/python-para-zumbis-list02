#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
a1 =float(input(' Peso do peixe? '))
if a1 <= 50:
    print('Peso normal, sem multa! ')
elif a1 > 50:
    print('A cima do peso, multa a pagar')

a10 = a1 - 50

a12 = a10*4

print('Você passou {} kg do peso indicado '.format(a10))

print('Você deverar pagar R${} em multa'.format(a12))
