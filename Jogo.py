import random


def obter_escolha_usuario():

    jogador = input("Escolha: pedra (1), papel(2) ou tesoura(3)")
    if jogador == "1":
        return "pedra"
    elif jogador == "2":
        return "papel"
    elif jogador == "3":
        return "tesoura"
    else:
        print ("Escolha inválida. Por favor digite 1, 2 ou 3")
        


def gerar_escolha_computador():

    jogo = ["Pedra", "Papel", "Tesoura"]
    computador = random.randint(0,2)    
    print ("Escolha do computador:{}".format(jogo[computador]))
    return computador


 

    





def determinar_vencedor(j, c):
<<<<<<< HEAD
    if j == "pedra":
        if c == 0:
            print ("Empate")
        elif c == 1:
            print ("O computador ganhou")
        elif c == 2:
            print("Parabéns. Você ganhou")

            
    elif j == "papel":
        if c == 0:
            print ("Parabéns. Você ganhou")
        elif c == 1:
            print ("Empate")
        elif c == 2:
            print("O computador ganhou")
    
    elif j == "tesoura":
        if c == 0:
            print ("O computador ganhou")
        elif c == 1:
            print ("Parabéns. Você ganhou")
        elif c == 2:
            print("Empate")
    
=======
    pass
>>>>>>> efcdf8654c40def64faa7d25ce154660331af7c3








<<<<<<< HEAD
=======

>>>>>>> efcdf8654c40def64faa7d25ce154660331af7c3
def jogar_novamente():
    print("Deseja jogar novamente?")
    jogador = input("Digite sim ou não: ")
    if jogador == "sim":
        return jogo()
    else:
        return  print("que pena, nos vemos em breve"), exit()
        
    
        







def main():
    
    while True:
        print("-="*10)
        print("Jokenpo")
        print("-="*10)
        print("Vamos jogar?")
        us_digit= input("digite sim ou não: ")

        if  us_digit == "sim":
           jogo()
            
        elif us_digit == "não":
            print("que pena, nos vemos em breve")
            break
        
        else:
            print(f"opção {us_digit} invalida. Digite apenas sim ou não")

      

def jogo():

    j = obter_escolha_usuario()
    c = gerar_escolha_computador()
    determinar_vencedor(j, c)
    jogar_novamente()


if __name__=="__main__":
    main()