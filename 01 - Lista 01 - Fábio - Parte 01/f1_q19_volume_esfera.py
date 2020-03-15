# 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14).
# ENTRADA 
r = float(input('Informe o valor do raio: '))
p = float(3.14)

# PROCESSAMENTO
v = ((4*p*(r**3))/3)

# SAÍDA
print (f'O valor do volume é {v}.')