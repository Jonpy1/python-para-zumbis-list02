#Determine se um ano é bissexto.
a1 = int(input("Digite o ano: "))

if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0:
    print("{} é ano bissexto.".format(a1))
else:
    print("{} NÃO é ano bissexto.".format(a1))