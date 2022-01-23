def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    ava_usuario = ava_computador = jogada = 0
    
    if n%(m+1) == 0:
        print()
        print("Você começa!")
        print()
        jogada = usuario_escolhe_jogada(n, m)
        n = (n - jogada)
        ava_usuario = 1
    else:
        print()
        print("Computador começa!")
        print()
        jogada = computador_escolhe_jogada(n, m)
        n = (n - jogada)
        ava_computador = 1
    print("Agora restam",n,"peças no tabuleiro")
    print()
    if (ava_computador == 1) and (ava_usuario == 0):
        i = 1
        while n > 0:
            if (ava_computador + i)%2 == 1:
                retirada = int(computador_escolhe_jogada(n,m))
                n = (n - retirada)
                print()
                print("O computador tirou",retirada,"peça")
            elif (ava_usuario + i)%2 == 1:
                retirada = int(usuario_escolhe_jogada(n,m))
                n = n - retirada
            i = i + 1
            if n > 0:
                print("Agora restam",n,"peças no tabuleiro")
            retirada = 0
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
    elif ava_computador == 0 and ava_usuario == 1:
        i = 1
        while n > 0:
            if (ava_computador + i)%2 == 1:
                retirada = computador_escolhe_jogada(n,m)
                n = (n - retirada)
                print()
                print("O computador tirou",retirada,"peça")
            elif (ava_usuario + i)%2 == 1:
                retirada = usuario_escolhe_jogada(n,m)
                n = (n - retirada)
            i = i + 1
            if n > 0:
                print("Agora restam",n,"peças no tabuleiro")
            retirada = 0
        if n == 0:
            print("Fim do jogo! O computador ganhou!")

    return
def computador_escolhe_jogada(n, m):
    maior_multiplo = jogada =  0
    i = 1
    if n - m <= 0:
        jogada = n
        return jogada
    else:
        while i <= n:
            if ((n-i)%(m+1)== 0) and (n-i >= m) and (i <= m):
                maior_multiplo = i
            i = i + 1
        print("O computador tirou ",maior_multiplo,"peça.")
        if maior_multiplo != 0:
            jogada = maior_multiplo
        else:
            jogada = m
    return jogada

def usuario_escolhe_jogada(n, m):
    print()
    usuario = int(input("Quantas peças você vai tirar? "))   
    if usuario <= m and usuario>0:
        print()
        print("Você tirou ",usuario,"peça.")
        return int(usuario)
    else:
        print()
        print("Oops ! Jogada inválida! Tente de novo.")
        usuario = usuario_escolhe_jogada(n, m)
        return int(usuario)
    print("Valor de jogada usuario antes de sair da função usuario_escolhe: ",usuario)

def main():
    escolha = -1
    i = 1
    
    while escolha != 1 and escolha != 2:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print()
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input())
    if escolha == 1:
        print("Você escolheu uma partida!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        while i <= 3:
            print()
            print("**** Rodada",i,"****")
            print()
            partida()
            i = i + 1
        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você 0 x ",i,"computador")
main()

# 31, in partida / n = (n - retirada) / TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'

    
            
        
