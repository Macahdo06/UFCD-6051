#ciclo principal

while True:
    #dados de entrada
    deposito_de_combustivel = 100

    #processamento
    if deposito_de_combustivel < 20:
        ligar_luz_de_reserva = True
    else:
        ligar_luz_de_reserva = False