# 20. Um sistema de equações lineares do tipo  , pode ser resolvido segundo mostrado abaixo:
# ENTRADA
a = int(input('Insira o a: '))
b = int(input('Insira o b: '))
c = int(input('Insira o c: '))
d = int(input('Insira o d: '))
e = int(input('Insira o e: '))
f = int(input('Insira o f: '))

# PROCESSAMENTO
x = ((c*e - b*f) / (a*e - b*d))
y = ((a*f - c*d) / (a*e - b*d))

# SAIDA
print(f'O valor de x é {x:.2f} e o valor de y é {y:.2f}.')