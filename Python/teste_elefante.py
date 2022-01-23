def incomodam(n):
    texto = 'incomodam '
    vazio = ''
    if n == 1:
        return texto
    if n > 1:
        return texto + incomodam(n - 1)
    else:
        return vazio

def elefantes(n, x=1, s="", ee=" elefantes incomodam muita gente"):
    if n <= 1 and x == 1:
        return s
    else:
        if x == n:
            return print(str(n) + " elefantes", incomodam(n), "muito mais")
        else:
            if x > 1:
                print(str(x) + ee, end="\n")
            else:
                print("Um elefante incomoda muita gente", end="\n")
            if x < n - 1:
                print(str(x + 1) + " elefantes", incomodam(x + 1), "muito mais", end="\n")
            return elefantes(n, x + 1)

# Estava na funcao elefantes(n)
def elefantes(n):
    if n < 1:
        return ""
    if n == 1:
        return 'Um elefante incomoda muita gente' 
    else:
        return elefantes(n-1) + str(n)+ " " + "elefantes" + " " + incomodam(n) + "muito mais \n" + str(n) + " " + "elefantes incomodam muita gente"
