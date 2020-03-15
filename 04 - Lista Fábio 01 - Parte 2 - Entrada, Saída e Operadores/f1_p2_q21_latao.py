# 21.	Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses 
# componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.
# ENTRADA
l = float(input('Insira a quantidade de latão em kg: '))

# PROCESSAMENTO
c = (70*l)/100
z = (30*l)/100

# SAIDA
print(f'A quantidade de cobre é de {c} kgs, a de zinco é {z} kgs, totalizando {l} kgs de latão.')