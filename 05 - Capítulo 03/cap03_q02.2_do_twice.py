# Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um 
# argumento.
def do_twice (f,g):
    f(g)
    f(g)
    
def print_f (valor):
    print(valor)

do_twice(print_f, "Pedro")

