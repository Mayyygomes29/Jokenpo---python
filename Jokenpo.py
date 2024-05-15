from time import sleep
import random

#JOKENPÔ
print("Suas Opções:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

print("JOOO")
sleep(1)
print("kenn")
sleep(1)
print("PÔÔÔÔÔ")
jogador = int(input("Escolha sua opção: "))

pc = random.randint(0,2)

if pc == 0: #pedra
    if jogador ==0:
        print("EMPATE!")
        print("A maquina escolheu {} e você {}".format(pc, jogador ))
    elif jogador == 1:
        print("Papel enrola pedra. VOCÊ GANHOU!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))
    elif jogador == 2:
        print("Pedra bate na tesoura. O COMPUTADOR GANHOU!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador )) 
    else :
        print("JOGADA INVÁLIDA!")
        print("Tente novamente.")        
elif pc == 1: #papel
    if jogador == 0:
        print("Papel enrola pedra. O PC GANHOU!!!")   
        print("A máquina escolheu {} e você {}".format(pc, jogador ))       
    elif jogador == 1:
        print("EMPATE!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))
    elif jogador == 2:
        print("Tesoura corta papel. VOCÊ GANHOU!!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))
    else :
        print("JOGADA INVÁLIDA!")
        print("Tente novamente.")       
elif pc == 2:   #tesoura 
    if jogador == 0:
        print("Pedra bate na tesoura. VOCÊ GANHOU!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))
    elif jogador == 1:
        print("Tesoura corta papel. O PC GANHOU!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))  
    elif jogador == 2:
        print("EMPATOU!!!")
        print("A máquina escolheu {} e você {}".format(pc, jogador ))    
    else :
        print("JOGADA INVÁLIDA!")
        print("Tente novamente.")    