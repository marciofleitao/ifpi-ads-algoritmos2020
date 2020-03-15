# 4. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de segundos: '))

# PROCESSAMENTO 
hr = n//3600
resto = n%3600
min = resto//60
sg = resto%60

# SAÍDA
print(f'{n} segundos equivalem a {hr} horas, {min} minutos e {sg} segundos.')
