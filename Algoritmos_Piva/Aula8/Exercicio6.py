palavra = input("Digite a palavra: ")
inverso_palavra = palavra[::-1]

if palavra.lower() == inverso_palavra.lower():
    print(f"A frase {palavra} é Palindromo!")
else:
    print(f"A palavra {palavra} NÃO é palindromo!")