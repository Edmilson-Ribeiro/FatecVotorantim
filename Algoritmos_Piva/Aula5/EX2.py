nota1 = float(input("Insira aqui a nota1: "))
nota2 = float(input("Insira aqui a nota2: "))
nota3 = float(input("Insira aqui a nota3: "))
media = (nota1 + nota2 + nota3) / 3

if media < 3:
    Resultado = ("Reprovado")
    else:
    if media < 7:
        Resultado = ("Exame"nota_exame = 12 - media)
        else:
        resultado = ("Aprovado")
        print(f"Média {media: 5.2f} - {Resultado}!")
        if nota_exame != 0:
            print(f"Tem que tirar no minimo {nota_exame: 5.2f}")
