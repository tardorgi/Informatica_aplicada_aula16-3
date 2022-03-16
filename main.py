#pedindo valores ao usuário
hora=int(input('Quantas horas você correu?\n'))
minutos=int(input('e quantos minutos?\n'))
segundos=int(input('e os segundos?\n'))

#retorno do tempo em segundos
tempo=(3600 * hora) + (60 * minutos) + segundos
print ('você correu',tempo,'segundos')

#pedido de valores + conta para metros
distancia=int(input('Quantos Km você correu?\n'))
distanciametros=(1000 * distancia)
print('você correu',distanciametros,'metros')

#calculo de velocidade média
velocidademedia=int(distanciametros/tempo)
print('Sua velocidade média foi de',velocidademedia,'m/s')
  