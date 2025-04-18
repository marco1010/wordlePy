import functions

retries = 5
target = "TORRE"

print("WORDLE: ADIVINA LA PALABRA DE 5 LETRAS")
print("Tenes 5 intentos.")

while retries > 0:
    line = input("Ingresa una palabra: ")
    print(functions.checkWord(line, target))
    if line == target:
        print("FELICIDADES! Acertaste la palabra!")
        break
    retries = retries - 1
    print(f"Te quedan {retries} intentos")

if retries == 0:
    print("PERDISTE. Te quedaste sin intentos.")
