def segundos(h, m, s):
    return (hora * 3600 * minuto * 60 * segundo)

hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo= int(input("Digite o segundo: "))

print(f"O total de segundos é {segundos(hora,minuto,segundo)}")