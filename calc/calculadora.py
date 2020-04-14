import msvcrt
num1 = int(input("Dijite un numero: "))
num2 = int(input("Otra vez: "))
resta = num1 - num2
suma = num1 + num2

pregunta = int(input("PARA RESTA ESCRIBA 1 Y PARA SUMA 2 "))

if pregunta == 1:
    print(resta)
if pregunta == 2:
    print(suma)
msvcrt.getch()
