# 6.	Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
# ENTRADA
velocidade_kmh = float(input('Informe a velocidade e km/h: '))

# PROCESSAMENTO 

velocidade_ms = velocidade_kmh / 3.6

# SAIDA

print (f'{velocidade_kmh} km/h equivalem a {velocidade_ms} m/s')