#2- Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
quant = int(input("Digite a quantidade de alunos que irão votar: "))
print("-------------------------------")
print("DIAS A SEREM ESCOLHIDOS:")
print("1 - SEGUNDA-FEIRA \n2- TERÇA-FEIRA \n3- QUARTA-FEIRA \n4- QUINTA-FEIRA \n5- SEXTA-FEIRA\n")

seg = 0
ter = 0
qua = 0
qui = 0
sex = 0
i = int(0)
for i in range (i, quant):
    count = i + 1
    vot = int(input("Aluno nº {}, digite a opção desejada: ".format(count)))
    if vot == 1:
        seg = int(seg + 1)
    elif vot == 2:
        ter = int(ter + 1)
    elif vot == 3:
        qua = int(qua + 1)
    elif vot == 4:
        qui = int(qui + 1)
    elif vot == 5:
        sex = int(sex + 1) 
    else:
        print("POR FAVOR DIGITE UM DIA VALIDO")
    
print("\nQUANTIDADE DE VOTOS: ")
print("SEGUNDA-FEIRA: {} votos \nTERÇA-FEIRA: {} votos \nQUARTA-FEIRA: {} votos \nQUINTA-FEIRA: {} votos \nSEXTA-FEIRA: {} votos \n".format(seg, ter, qua, qui, sex))