import principal

A= True
B= False


Saida = not ((A and not B) or (not A and B))


Saida1 = principal.xnor(A, B)

C = True
D = False

Saida2 = principal.xnor (C, D)

