secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Insira um número: "))

while number != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    number = int(input("Tente de novo, insira um número: "))

print("O número secreto é: ", secret_number, "!", sep="")
print("Muito bem, trouxa! Você está livre agora.")