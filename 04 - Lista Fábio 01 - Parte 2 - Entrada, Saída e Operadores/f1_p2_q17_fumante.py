# 17. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros 
# fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).
# ENTRADA
a = float(input('Insira o número de anos que ele fuma: '))
n = int(input('Insira o número de cigarros fumados por dia: '))
p = float(input('Insira o preço de uma carteira: R$ '))

# PROCESSAMENTO
g = (a*365) * (n) * (p/20)

# SAIDA
print(f'Um fumante gasta uma quantidade de R${g:.2f}.')