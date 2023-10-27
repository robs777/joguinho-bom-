#   1° obter_escolha_usuario 

#   2° gerar_escolha_computador 

import random

Mylist = ["Pedra", "Papel", "Tesoura"]

#função
def gerar_escolha_computador(A,B,C):
    
    AS = "Pedra"
    BS = "Papel"
    CS = "Tesoura"
    computador = random.choices(Mylist(A, B, C))


###########################################
#código principal

AS = "Pedra"
BS = "Papel"
CS = "Tesoura"
print(gerar_escolha_computador(AS, BS, CS))

#   3° determinar_vencedor 

#   4° jogar_novamente 