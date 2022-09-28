# calcular horario de final de evento
# teniendo hora de inicio y duración

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minu = (mins + dura) % 60
hour = (hour + (mins+dura)//60) % 24
print(hour, ":" , minu)
