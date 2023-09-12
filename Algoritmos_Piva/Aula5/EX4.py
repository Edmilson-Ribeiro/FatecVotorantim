x = float(input("Entre com o x "))
y = float(input("Entre com o y "))
z = float(input("Entre com o z "))

if ((x+y > z) and (x+z > y) and (y+z > x)):
# é um triângulo
if (x == y ==z):
    print("É um triângulo equilátero!!")
elif((x == y)or(x == z)):
    print("É um triângulo isósceles!!")
else:
    print("É um triângulo escaleno!!")
else: x não é um triângulo
print("Os lados não formam um triângulo!!")


