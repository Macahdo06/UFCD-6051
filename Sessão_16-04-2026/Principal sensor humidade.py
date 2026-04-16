#ciclo principal

while True:
    #dados de entrada
    tulipa = 1
    cacto = 2
    sensor_humidade = 50
    tempo = 3 #dias

    #processamento
    if tulipa == cacto and sensor_humidade < 50 and tempo > 3:
        ligar_rega = True
    else:
        ligar_rega = False