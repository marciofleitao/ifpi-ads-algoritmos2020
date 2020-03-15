# 9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).
# ENTRADA
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

#PROCESSAMENTO 
leitura_direta = (num1,num2)
leitura_inversa = (num2,num1)

#SAÍDA
print(f'A ordem direta dos números, segundo a sua inserção, é {leitura_direta} e a ordem inversa {leitura_inversa}.')