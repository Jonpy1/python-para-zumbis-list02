#faça um programa que leia três numeros e mostre o maior e o menor deles
a1 = int(input('Digite um numero: '))
a2 = int(input('Digite outro numero: '))
a3 = int(input('Digite mais um numero: '))

if (a1 < a2) or (a1 < a3):
  print('O menor valor é {}'.format(a1))
elif (a2 < a1) and (a2 < a3):
  print('O menor valor é {}'.format(a2))
elif (a3 < a1) and (a3 < a2):
  print('O menor valor é {}'.format(a3))

if (a1 > a2) or (a1 > a3):
  print('O maior valor é {}'.format(a1))
elif (a2 > a1) and (a2 > a3):
  print('O maior valor é {}'.format(a2))
elif (a3 > a1) and (a3 > a2):
  print('O maior valor é {}'.format(a3))
