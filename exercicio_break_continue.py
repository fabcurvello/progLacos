import random

print( "\n--- TESTE DE ADIVINHAÇÃO ---")
print("Você terá 5 tentativas para adivinhar o número oculto.")
print("Só valem números entre 1 e 20. Boa sorte!")

oculto = random.randrange(1,21)
#oculto = 7
for contador in range (1,6):
    numero = int(input(f"\nTentativa {contador} de 5:"))

    if ( (numero < 1) or (numero > 20) ):
        print("ATENÇÃO: O número a inserir precisa estar entre 1 e 20. Você perdeu esta tentativa.")
        continue

    if ( numero == oculto ):
        print (f"PARABÉNS! Você acertou na tentativa {contador}. O número oculto é {numero}.")
        break
    elif ( numero > oculto ):
        print(f"Você ERROU. O número oculto é menor que {numero}.")
    else:
        print(f"Você ERROU. O número oculto é maior que {numero}.")

    if ( contador == 5 ):
        print (f"Fim das tentativas! O número oculto que você não encontrou é {oculto}.")

print("\n--- FIM DO TESTE DE ADIVINHAÇÃO ---")
