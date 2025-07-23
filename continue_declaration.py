palavra = input("Insira uma palavra: ")

for l in palavra.upper():
    if l in ("A", "E", "I", "O", "U"):
        continue
    else:
        print(l, end="")
