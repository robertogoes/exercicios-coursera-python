def cria_matriz(num_linha, num_coluna):
    matriz = []
    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            valor = int(input())
            linha.append(valor)
        print(linha, "\n")

    return
