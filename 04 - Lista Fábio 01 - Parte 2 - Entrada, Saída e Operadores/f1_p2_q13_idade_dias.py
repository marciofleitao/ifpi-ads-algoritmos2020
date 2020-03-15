# 13. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.
# ENTRADA
n1 = int(input('Digite os anos: '))
n2 = int(input('Digite os meses: '))
n3 = int(input('Digite os dias: '))

# PROCESSAMENTO 
anos = n1*365
mes = n2*30
dias = int(anos+mes+n3)

# SAÍDA
print(f'A idade {n1} anos, {n2} meses e {n3} dias equivalem a {dias} dias.')