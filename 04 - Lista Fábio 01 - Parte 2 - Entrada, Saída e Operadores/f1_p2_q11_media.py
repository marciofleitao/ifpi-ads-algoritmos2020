# 11. Leia 3 números, calcule e escreva a média dos números.
# ENTRADA
n = int(input('Digite um número de três dígitos: '))

# PROCESSAMENTO 
c = n//100
d = (n%100)//10
u = (n%100)%10

media = (u+d+c)/3

# SAÍDA
print(f'A média dos algarismos de {n} é {media}.')