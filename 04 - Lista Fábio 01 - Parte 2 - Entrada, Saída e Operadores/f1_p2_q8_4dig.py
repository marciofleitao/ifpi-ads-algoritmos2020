# 8. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.
# ENTRADA
n = int(input('Digite um número inteiro de quatro dígitos binários: '))

# PROCESSAMENTO 
mil = n//1000
cem = (n%1000)//100
dez = ((n%1000)%100)//10
uni = ((n%1000)%100)%10

pri = uni*(2**0)
seg = dez*(2**1)
ter = cem*(2**2)
qua = mil*(2**3)

soma = pri+seg+ter+qua

# SAÍDA
print(f'O binário {n} equivale ao decimal {soma}.')