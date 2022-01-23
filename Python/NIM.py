
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while n!=0:
        if n%(m+1) == 0:
            print("Você começa!")
            resultado = usuario_escolhe_jogada(n, m)
        else:
            print("Computador começa!")
            resultado = computador_escolhe_jogada(n, m)
        n = n - resultado
    return

def computador_escolhe_jogada(n, m):
    if (n-m)%(m+1)== 0:
        quantidade_pecas_removidas = 1
    else:
        quantidade_pecas_removidas = n - m
        print("O computador tirou")
    return quantidade_pecas_removidas

def usuario_escolhe_jogada(n, m):
    jogada = 1
    while not(jogada <= m):
        jogada = int(input("Por favor, digite um valor a ser retirado: "))

def main():
    i = 1
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input())
    if escolha == 1:
        partida()
    elif escolha == 2:
        while i <= 3:
            partida()
            i = i + 1
    else:
        main()

    
            
        
