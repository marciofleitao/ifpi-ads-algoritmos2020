# 12. Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.
# ENTRADA
sal = float(input('Digite o valor de seu salário: '))

# PROCESSAMENTO 
aumento_sal = sal + (sal*(25/100))

# SAÍDA
print(f'O valor do salário é {sal}, após o aumento de 25% passará a ser {aumento_sal}.')