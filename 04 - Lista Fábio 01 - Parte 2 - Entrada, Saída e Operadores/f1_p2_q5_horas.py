# 5. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.
# ENTRADA
n = int(input('Digite um número inteiro de horas: '))

# PROCESSAMENTO 
semana = n//168
dias = (n%168)//24
hr = (n%168)%24

# SAÍDA
print(f'{n} horas equivalem a {semana} semanas, {dias} dias e {hr} horas.')