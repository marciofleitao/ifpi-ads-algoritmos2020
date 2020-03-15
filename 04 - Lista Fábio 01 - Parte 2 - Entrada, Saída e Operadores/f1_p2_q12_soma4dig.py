# 12. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: 
# número = 9534 ; soma = 9+5+3+4 = 21.
# ENTRADA
n = int(input('Digite um número de quatro dígitos: '))

# PROCESSAMENTO 
m = n//1000
c = (n%1000)//100
d = ((n%1000)%100)//10
u = ((n%1000)%100)%10
soma = m+c+d+u

# SAÍDA
print(f'A média dos algarismos de {n} é {soma}.')