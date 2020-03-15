# 19. Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva 
# a distância entre eles, conforme formula abaixo.
# ENTRADA
x1 = float(input('Insira o x1: '))
y1 = float(input('Insira o y1: '))
x2 = float(input('Insira o x2: '))
y2 = float(input('Insira o y2: '))

# PROCESSAMENTO
d = (((x2-x1)**2)+((y2-y1)**2))**0.5

# SAIDA
print(f'A distância é {d:.2f}.')