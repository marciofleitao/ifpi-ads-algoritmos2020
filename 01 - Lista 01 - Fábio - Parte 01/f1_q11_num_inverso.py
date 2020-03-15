# 11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)
# ENTRADA
num = int(input('Digite o número com três dígitos: '))

# PROCESSAMENTO
centena = int(num/100)
dezena = int((num % 100) // 10)
unidade = int(num)%((centena*100)+((dezena*10)))

# SAÍDA
print(f'O inverso do número {num} é {unidade}{dezena}{centena}.')