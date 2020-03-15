# 18. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao 
# custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de 
# fábrica de um carro e escreva o custo ao consumidor.
# ENTRADA
p = float(input('Insira o custo de fábrica: '))

# PROCESSAMENTO
d = (28*p)/100
i = (45*p)/100

soma = p+d+i

# SAIDA
print(f'O valor da carro novo é {soma}.')