from math import pow, sqrt
X1 = int(input("Entre com X1 "))
Y1 = int(input("Entre com Y1 "))
X2 = int(input("Entre com X2 "))
Y2 = int(input("Entre com Y2 "))
DX = X2 - X1
DY = Y2 - Y1

distancia = sqrt(pow(DX, 2) + pow(DY, 2))

print("A distância entre os pontos: ",distancia)
