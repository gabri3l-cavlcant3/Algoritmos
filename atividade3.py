#atividades comerciais de uma padaria.
#valor total de vendas 
a = float (input( 'valor do pao:'))

b = float (input('valor da broa:'))

C = int (input( 'quantidade de pao vendido;'))
D = int (input( 'quantidade de broa vendida:'))
resultado = a * C
resultado2 = b * D
resultado3 = resultado + resultado2
resultado4 = int resultado3 / 10

print ( 'valor de:', resultado )
print ('valor de:', resultado2 )
print ( 'valor total vendido:', resultado3)
print ('qauntidade a ser guardada:', resultado4)
