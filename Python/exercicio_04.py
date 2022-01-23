segundos = int(input("Digite aqui a quantidade de segundos: "))
dias = segundos//(3600*24)
segundos_hora = segundos%(3600*24)
horas = segundos_hora//3600
segundos_sobra = segundos%3600
minutos = segundos_sobra//60
segundos_final = segundos_sobra%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_final,"segundos.")
