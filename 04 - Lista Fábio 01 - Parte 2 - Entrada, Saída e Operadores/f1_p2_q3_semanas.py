# 3. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de dias: '))

# PROCESSAMENTO 
sem = n//7
d = n%7

# SAÍDA
print(f'O número inteiro {n} corresponde a {sem} semanas e {d} dias.')