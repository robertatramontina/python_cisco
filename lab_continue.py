palavra = input("Digite sua palavra aqui: ")
palavra = palavra.upper()
# Solicita que o usuário insira uma palavra
# e atribua-a à variável user_word.

for letter in palavra:
    if letter in ("A", "E", "I", "O", "U"):
    # Preenchao corpo do loop for.
        continue
    print(letter)