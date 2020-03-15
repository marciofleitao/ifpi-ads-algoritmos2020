# 5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).
# ENTRADA

numero = int(input('Digite o número: '))

# PROCESSAMENTO 
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero)%((centena*100)+((dezena*10))) 
soma = centena+dezena+unidade

# SAIDA
print(f'{centena} + {dezena} + {unidade} é igual a {soma}')
