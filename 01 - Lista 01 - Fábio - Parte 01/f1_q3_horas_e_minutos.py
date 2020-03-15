# 3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.
# ENTRADA

valor_min = int(input('Digite o valor em minutos: '))

# PROCESSAMENTO 
valor_h = valor_min // 60
valor_resto = valor_min%60

# SAIDA
print(f'{valor_min} minutos é igual a {valor_h} horas e {valor_resto} minutos')
