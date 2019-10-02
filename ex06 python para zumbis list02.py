#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo: a. + Salário Bruto : R$ b. - IR (11%) : R$ c. - INSS (8%) : R$ d. - Sindicato ( 5%) : R$ e. = Salário Liquido : R$ 

a2 = int(input('Quanto você ganha por horas? '))
a3 = int(input('Quantas horas você trabalha por mês? '))
salario = a2*a3
print('Seu salário bruto é de {}R$'.format(salario))
ir = salario * 0.11
inss= salario * 0.08
contsind = salario * 0.05
liquido = salario - ir - inss - contsind

print('desconto de IR {}'.format(ir))
print('desconto de  INSS {}'.format(inss))
print('desconto de SINDICADO {}'.format(contsind))
print('Seu salario liquido é de R$ {}'.format(liquido))
