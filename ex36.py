'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


Casa = int(input('Digite o valor da casa'))
Salario = int(input('Qual o seu salário ?'))
Anos = int(input('Em quantos anos deseja pagar ?'))
Meses = Anos * 12
Mensalidade = Casa / Meses
mínimo = Salario * 30 /100

print('Para pagar a casa de R${:.2f} em {} anos  '.format(Casa , Anos) , end ='')
print('a Prestação será de R$ {:.2f}'.format(Mensalidade))

if Mensalidade <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO !')





'''print(' O valor da Mensalidade Para a Prestação da casa é  {:.2f}'.format(Mensalidade))'''

