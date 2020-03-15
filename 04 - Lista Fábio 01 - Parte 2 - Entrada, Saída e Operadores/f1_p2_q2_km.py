# 2. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de metros: '))

# PROCESSAMENTO 
km = n//1000
m = n%1000

# SAÍDA
print(f'O número inteiro {n} corresponde a {km} quilômetros e {m} metros.')