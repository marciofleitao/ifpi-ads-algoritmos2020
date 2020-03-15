# 10.	Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso. 
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).
# ENTRADA
n = int(input('Digite um número de três dígitos: '))

# PROCESSAMENTO 
c = n//100
d = (n%100)//10
u = (n%100)%10
inv = int(u*100+d*10+c)
soma = int(n+inv)

# SAÍDA
print(f'O inverso de {n} é {u}{d}{c} e a soma dos dois é {soma}.')