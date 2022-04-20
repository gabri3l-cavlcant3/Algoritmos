# Informar o valor do preço da gasolina e quanto foi gasto para abastecer.
Valor = float (input('informe o valor do litro da gasolina:'))
Preco = float (input('informe o valor do pagamento:'))

litros = Preco / Valor

#arredonda o valor de litros com 2 casas

arred = round (litros, 2)

print (arred, 'litros')




