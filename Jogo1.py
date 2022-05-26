print("Jogo pedra papel e tesoura...")
s1 = int(input("Jogador 1: Digite 1 para Pedra 2 para Papel e 3 para Tesoura: "))
s2 = int(input("Jogador 2: Digite 1 para Pedra 2 para Papel e 3 para Tesoura: "))


# empate
if (s1 == 1 and s2 == 1) or (s1 == 2 and s2 == 2) or (s1 == 3 and s2 == 3):
    print("Empatou.")
# S1 ganha
elif (s1 == 1 and s2 == 3) or (s1 == 2 and s2 == 1) or (s1 == 3 and s2 == 2):
    print("O jogador 1 ganhou.")
# S2 ganha
elif (s1 == 1 and s2 == 2) or (s1 == 2 and s2 == 3) or (s1 == 3 and s2 == 1):
    print("O jogador 2 ganhou.")
else:
    print("Inválido.")