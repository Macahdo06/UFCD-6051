quadro = {
    "corte_geral" : {
        "in"    :   32
    },

    "dijuntor"  :   {
        "in"    :   16,
        "in"    :   20,
    },

    "diferencial"   :   {
        "in"    :   32,
        "deltai"    :   0.03
    },

    "barramento"    :   {
        "terra"  :   100,
        "neutro"    :   100
    },

    "fio"   :   {
        "fase"  :   1.5,
        "neutro"    :   1.5,
        "terra" :   1.5
    },

    "fio"   :   {
        "fase"  :   2.5,
        "neutro"    :   2.5,
        "terra" :   2.5
    },
   
}

lampadas = {
    "potencia"  :   40,
    "tensao"    :   230,
    "quantidade"    :   3
}

import minhas_funcoes

corrente_de_cada_lampada = minhas_funcoes.calcular_corrente(lampadas["potencia"]  /   lampadas["tensao"])
print("corrente_de_cada_lampada")

corrente_de_todas_as_lampadas = minhas_funcoes 
print("corrente_de_todas_as_lampadas")


minhas_funcoes.selecionar_dijuntor(corrente_de_todas_as_lampadas)
