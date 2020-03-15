# 16. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# ENTRADA
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

# PROCESSAMENTO
r = (a+b)**2
s = (b+c)**2
d = (r+s)/2

# SAIDA
print(f'O valor da expressão é {d}.')

