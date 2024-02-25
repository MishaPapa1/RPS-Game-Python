import random

punctaj_jucator = 0
punctaj_ai = 0

while punctaj_ai < 2 and punctaj_jucator < 2:
    r = random.randrange(0,3)
    user_input = input("Ce alegi dintre Piatra, Hartie si Foarfeca: \n")
    jucator=user_input.lower()
    match jucator:
        case "piatra":
            if r == 0:
                print("Ai castigat runda.\n")
                punctaj_jucator += 1
            elif r == 1:
                print("Ai pierdut runda.\n")
                punctaj_ai += 1
            else:
                print("Este egal.\n")

    match jucator:
        case "hartie":
            if r == 0:
                print("Ai pierdut runda.\n")
                punctaj_ai += 1
            elif r == 1:
                print("Este egal.\n")
            else:
                print("Ai castigat runda.\n")
                punctaj_jucator += 1

    match jucator:
        case "foarfeca":
            if r == 0:
                print("Este egal.\n")
            elif r == 1:
                print("Ai castigat runda.\n")
                punctaj_jucator += 1
            else:
                print("Ai pierdut runda.\n")
                punctaj_ai += 1

    print("Ai " + str(punctaj_jucator) + " puncte.\nAI-ul are " + str(punctaj_ai) + " puncte.\n")

if punctaj_ai == 2:
    print("AI-ul a castigat meciul.")
else:
    print("Ai castigat meciul.")