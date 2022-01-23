def funcao_binomial(n,k):
    valor = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return valor 

    
def fatorial(x):
    i = 1
    resultado = 1
    while i <=x:
        resultado = resultado*i
        i = i + 1
    return resultado



        
