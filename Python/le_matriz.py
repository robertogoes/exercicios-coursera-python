def cria_matriz(num_linha, num_coluna):
    matriz = []
    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "] da matriz: "))
            linha.append(valor)

        matriz.append(linha)
    for i in matriz:
        for j in i:
            print(j, end =" ")
        print()

    return 

def le_matriz():
    resultado = []
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    resultado = cria_matriz(lin, col)
    
    return resultado

# TÁ FALTANDO IMPRIMIR A MATRIZ UMA LINHA ABAIXO DA OUTRA
