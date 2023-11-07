d = {}

for _ in range(5):
    nome = input("entre com o sobrenome: ")
    idade = int(input("entre com a idade: "))
    d[nome] = idade

maior_sobrenome = ""
maior_idade = 0
for chave, valor in d.items():
    if valor > maior_idade:
        maior_idade = valor
        maior_sobrenome = chave

print(f"O sobrenome {maior_sobrenome} possui a maior idade {maior_idade}")
