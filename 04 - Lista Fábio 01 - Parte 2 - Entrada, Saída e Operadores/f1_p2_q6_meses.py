# 6. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de meses: '))

# PROCESSAMENTO 
anos = n//12
meses = n%12


# SAÍDA
print(f'{n} meses equivalem a {anos} anos e {meses} meses.')