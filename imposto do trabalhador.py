hora = int(input('Digite o valor da sua hora de trabalho:'))
salario = hora * 8 * 5 * 4
salarioBruto = salario

if salario <= 900:
    aux = 0

elif salario > 900 and salario <= 4000:
    salario = salario - salario * 0.08
    aux = 8

else:
    salario = salario - salario * 0.13
    aux = 13

salario = salario - salario * 0.09
salario = salario - salario * 0.08

print('=-='*10)
print('IMPOSTO DO TRABALHADOR')
print('---'*10)
print(f'Valor do salário bruto: R${salarioBruto:.2f}')
print('---'*10)
print('IMPOSTOS:')
print(f'Desconto do IMPOSTO DE RENDA: {aux}%')
print('Desconto do ICMS: 9%')
print('Desconto do IPVA: 8%')
print('---'*10)
print(f'Valor do salário líquido: R${salario:.2f}')
