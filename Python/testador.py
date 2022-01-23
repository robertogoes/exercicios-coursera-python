n = int(input("Digite o número de alunos"))
i = 1
somador = 0

while i <=n:
    nota = float(input("Digite a nota final do aluno "))
    if (nota>3) and (nota<5):
        somador = somador + 1
    i = i + 1

print("A quantidade de alunos em recuperação é:",somador)