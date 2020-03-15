# 14. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.
# ENTRADA
n = int(input('Digite a idade em dias: '))

# PROCESSAMENTO 
a = n//365
m = (n%365)//30
d = (n%365)%30

# SAÍDA
print(f'A idade {n} dias equivale a {a} anos, {m} meses e {d} dias.')