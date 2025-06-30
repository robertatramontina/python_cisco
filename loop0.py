largest_number = -999999999

number = int(input("Digite um número ou -1 para parar: "))

while number != -1:

    if number > largest_number:
        largest_number = number
    number = int(input("Digite um número ou digite -1 para parar: "))

print("O maior número é: ", largest_number)        
#Ir para a linha 02
        
