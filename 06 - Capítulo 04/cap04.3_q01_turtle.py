# Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.

def square(t):
    import turtle
    mf = turtle.Turtle()
    mf.shape("turtle")
    for i in range(4):
        mf.fd(100)
        mf.lt(90)
    
    turtle.mainloop()

square('t')

















