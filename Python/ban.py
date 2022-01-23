def compara_assinatura(as_a, as_b):
        '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
        i = len(as_b)
        print(i)
        j = 0
        absoluto = 0
        while j < i:
                absoluto = absoluto + abs(as_a[j]-as_b[j])
                print("J: ", j)
                print()
                print(abs(as_a[j]-as_b[j]))
                print()
                j += 1
                print(absoluto)
        sab = absoluto/6
                        
        return sab
