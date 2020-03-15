# 22. Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o numero de notas de cada valor 
# que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as 
# notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de 
# R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota
# de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com 
# o critério da distribuição ótima.
# ENTRADA
v = int(input('Qual o valor do saque: .'))

# PROCESSAMENTO
cem = v//100
cinq = (v%100)//50
vinte = ((v%100)%50)//20
dez = (((v%100)%50)%20)//10
cinco = ((((v%100)%50)%20)%10)//5
dois = (((((v%100)%50)%20)%10)%5)//2

# SAIDA
print(f'Serão sacadas {cem} nota de cem, {cinq} notas de cinquenta, {vinte} notas de vinte, {dez} notas de dez, {cinco} notas de cinco reais e {dois} notas de dois reais.')


