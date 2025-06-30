# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i) #quando encontrar esse valor, saia
print("Fora do loop.")          #no caso imprime os resultados menos o 3 vai para a instrucao posterior


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i) #qdo chegar nesse valor, ja é suficiente
print("Fora do loop.")          #aqui nao imprime o 3 qdo chega nele, pula e segue pra seguinte

