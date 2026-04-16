#ciclo principal

while True:
    #dados de entrada
    indicador_de_bateria = 100
    
    #processamento
    if indicador_de_bateria <= 20:
        ligar_carregador = True
    else:
        ligar_carregador = False