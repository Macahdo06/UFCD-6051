#ciclo principal

while True:
    #dados de entrada
    sensor_1 = 100
    sensor_2 = 100
    sensor_3 = 100
    sensor_4 = 100

    #processamento
    if sensor_1 <= 40 or sensor_2 <= 40 or sensor_3 <= 40 or sensor_4 <= 40:
        ligar_luzes = True
    else:
        ligar_luzes = False