frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")
qtd = frase.count(palavra)
total_palavras = frase.count(' ') + 1

print(f"A frase possui um total de {total_palavras} palavras!")
print(f"A palavra {palavra} foi encontrada {qtd} vezes na frase")


