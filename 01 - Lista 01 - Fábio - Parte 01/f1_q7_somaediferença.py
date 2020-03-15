# 7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.
# ENTRADA
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# PROCESSAMENTO 
soma = num1 + num2
dif = num2 - num3

# SAIDA
print(f'A soma de {num1} + {num2} equivale a {soma} e a diferença de {num2} - {num3} equivale a {dif}.')
