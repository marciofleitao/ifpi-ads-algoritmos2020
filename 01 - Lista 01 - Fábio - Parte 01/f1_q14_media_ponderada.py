# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.
# ENTRADA
n1 = float(input('Digite a primeira nota: '))
p1 = int(input('Digite o primeiro peso: '))
n2 = float(input('Digite a segunda nota: '))
p2 = int(input('Digite o segundo peso: '))
n3 = float(input('Digite a terceira nota: '))
p3 = int(input('Digite o terceiro peso: '))

# PROCESSAMENTO
mp = float((n1*p1+n2*p2+n3*p3)/3)

# SAÍDA
print(f'O valor da média ponderada é {mp}.')