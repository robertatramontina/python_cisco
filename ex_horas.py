hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

saidaH = (hour*60 + mins + dura) // 60 % 24
saidaM = (hour*60 + mins + dura) % 60

print(saidaH, ":", saidaM, sep="")