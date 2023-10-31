import random


def obter_escolha_usuario():
    escolha_usuario = input("Escolha: pedra (1), papel(2) ou tesoura(3)")
    if escolha_usuario == "1":
        return "pedra"
    elif escolha_usuario == "2":
        return "papel"
    elif escolha_usuario == "3":
        return "tesoura"
    else:
        print ("Escolha inválida. Por favor digite 1, 2 ou 3")
        return obter_escolha_usuario()




def gerar_escolha_computador(escolha_usuario):
    pass
    





# def determinar_vencedor():




# def jogar_novamente():






def main():
    
    while True:
        print("-"*20)
        print("Jokenpo")
        print("-"*20)
        print("Vamos jogar?")
        us_digit= input("digite sim ou não")

        if  us_digit == "sim":
            abcd = obter_escolha_usuario()
            print(f"abcd == {abcd}")
            gerar_escolha_computador(abcd)
        
        elif us_digit == "não":
            print("que pena, nos vemos em breve")
            break
        
        else:
            print(f"opção {us_digit} invalida. Digite apenas sim ou não")




if __name__=="__main__":
    main()