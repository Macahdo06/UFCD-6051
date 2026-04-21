#ciclo principal
while True:

    #dados de entrada
    #janela com valores em percentagem
    janela1 = 50     #o valor pode ir de 0% a 100%
    janela2 = 40     #o valor pode ir de 0% a 100%

    #significa que quero verificar se a janela nao esta totalmente fechada
    if janela1 > 10 and janela1 < 90:

        print("janela 1 ok")
    else:
        print("janela 1 erro")



    if janela2 > 10 and janela2 < 90:
        print("janela 2 ok")
    else:
        print("janela 2 erro")
        