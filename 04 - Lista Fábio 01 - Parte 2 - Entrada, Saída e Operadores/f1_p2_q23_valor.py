# 23. Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a cada uma das duas prestações; 
# estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas prestações 
# são iguais a R$ 90,00; se o valor da mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00. Escreva 
# um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das duas prestações, de acordo com as regras acima.
# ENTRADA
v = float(input('Digite o valor da compra: R$'))

# PROCESSAMENTO
v_entrada = (v//3 + v%3)
v_parcela = (v-v_entrada)//2

# SAIDA
print(f'O valor da entrada é {v_entrada:.2f} e o valor das parcelas são {v_parcela:.2f}.')

