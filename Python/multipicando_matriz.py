
def multi_matrizes(A, B):
    num_lin_A, num_col_A = len(A), len(A[0])
    num_lin_B, num_col_B = len(B), len(B[0])
    #C = criando_matriz.cria_matriz(num_lin_A, num_col_B, 0)

    assert num_col_A == num_lin_B

    C = []
    for linha in range(num_lin_A):
        # começando uma nova linha
        C.append([])
        for coluna in range(num_col_B):
            # Adicionando uma nova coluna a linha
            C[linha].append(0)
            for k in range(num_col_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    
    return C

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(multi_matrizes(A, B))
            

    
    
