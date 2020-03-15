# 7. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de minutos: '))

# PROCESSAMENTO 
dias = n//1440
hr = (n%1440)//60
min = (n%1440)%60

# SAÍDA
print(f'{n} horas equivalem a {dias} dias, {hr} horas e {min} minutos.')