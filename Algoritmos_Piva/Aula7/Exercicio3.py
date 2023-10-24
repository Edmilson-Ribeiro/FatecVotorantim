for i in range(1,6):
    peso = float(input(f"Entre com o peso {i}: "))
    altura = float(input(f"Entre com a  altura {i}: "))
    imc = peso / (altura ** 2)
    print("Calcule o valor de imc: ", imc)