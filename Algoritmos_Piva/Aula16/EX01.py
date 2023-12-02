def calculo_patosecoelhos(total_cabecas, total_pes):
    patos = 0
    coelhos = 0

    for p in range(total_cabecas + 1):
        c = total_cabecas - p
        if 2*p + 4*c == total_pes:
            patos = p
            coelhos = c
            break
    return patos, coelhos

RA = int(input("Digite o RA: "))

Y = 23
total_cabecas = Y * 2 + 5
total_pes = total_cabecas * 2

patos_result, coelhos_result = calculo_patosecoelhos(total_cabecas, total_pes)
print("Total de patos:", patos_result)
print("Total de coelhos:", coelhos_result)