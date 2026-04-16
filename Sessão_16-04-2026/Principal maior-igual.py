#ciclo principal

while True:
    #dados de entrada
    sensor_de_pressao = 35

    #processamento
    if sensor_de_pressao >= 40:
        ligar_refrigeração = True
    else:
        ligar_refrigeração = False