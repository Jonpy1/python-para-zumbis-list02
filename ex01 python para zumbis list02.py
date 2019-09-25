#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
#Triângulo equilátero: possui os três lados com medidas iguais.
#Triângulo isósceles: possui dois lados com medidas iguais.
#Triângulo escaleno: possui os três lados com medidas diferentes.



#----------------------------------------------------------------------------------------------------------------

print('Digite as medidas do seu triângulo ')

a1= float(input('Qual a medida do primeiro lado? '))
a2= float(input('Qual a medida do segundo  lado? '))
a3= float(input('Qual a medida do terceiro lado? '))

if (a1 + a2 < a3) or (a1 + a3 < a2) or (a2 + a3 < a1):
    print('Nao é um triangulo')
elif (a1 == a2) and (a1 == a3) :
        print('Equilatero')
elif (a1==a2) or (a1==a3) or (a2==a3):
        print('Isósceles')
else:
        print('Escaleno')
