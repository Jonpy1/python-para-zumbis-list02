#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
metros = int(input('Quantos metros quadrados da área a ser pintada? '))
litros = metros / 3
capacidade = litros / 18
preço  = capacidade * 80
print('A quantidade de litros são de {:.0f}'.format(litros))
print('A quantidade de latas são de {:.0f}'.format(capacidade))
print('Total a pagar de {:.0f}'.format(preço))

