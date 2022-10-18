
print("for contador in range(1,10):")
for contador in range(1,10):
    print( contador )

print("\nfor contador in range(0, 10, 2):")
for contador in range(0, 10, 2):
    print(contador)

print("\nfor contador in [2, 3, 5, 7, 11, 13, 17, 19]:")
for contador in [2, 3, 5, 7, 11, 13, 17, 19]:
    print(contador)


mensagens = [
    "Olá Mundo!",
    "Python é melhor que Java",
    "Na verdade TUDO depende do Banco de Dados"
    "Alguém aqui falou em programação No Code?"
]

for mensagem in mensagens:
    print(mensagem)
    print("-----")


for indice, mensagem in enumerate(mensagens):
    print(f"{indice} - {mensagem}")
