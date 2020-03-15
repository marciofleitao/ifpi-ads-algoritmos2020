# 9. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.
# ENTRADA
n = int(input('Digite um número de três dígitos: '))

# PROCESSAMENTO 
c = n//100
d = (n%100)//10
u = (n%100)%10
dif = c-d-u

# SAÍDA
print(f'A diferença de {c}-{d}-{u} é {dif} e o inverso de {n} é {u}{d}{c}.')