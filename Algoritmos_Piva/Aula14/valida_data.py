from datetime import datetime
def valida_data(data_nasc):
    from datetime import datetime

    dia = int(data_nasc[0:2])
    mes = int(data_nasc[3:5])
    ano = int(data_nasc[6:])
    while dia > 31 or mes > 12:
        print("Data inválida")
        data_nasc = input("Digite a sua data de nascimento dd/mm/aaaa: ")

        dia = int(data_nasc[0:2])
        mes = int(data_nasc[3:5])
        ano = int(data_nasc[6:])

    data_nasc = datetime(ano,mes,dia).date()
    hoje = datetime.now().date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    if idade < 18:

        print(False)
    elif dia < 32:
        if mes < 13:
            if ano < 2023:
                print(True)





