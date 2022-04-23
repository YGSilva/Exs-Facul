#3- Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES:")
countImp = float(0)
for i in range (1, 51):
    if i % 2 == 1:
        ntImp = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
        countImp = countImp + ntImp

print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES:")
countPar = float(0)
for i in range (1, 51):
    if i % 2 == 0:
        ntPar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
        countPar = countPar + ntPar

medPar = countPar/25
medImp = countImp/25

print("\nMÉDIA DOS ALUNOS COM NÚMERAÇÃO ÍMPAR: {} PONTOS".format(round(medImp, 2)))
print("MÉDIA DOS ALUNOS COM NÚMERAÇÃO PAR: {} PONTOS".format(round(medPar, 2)))
if(medPar > medImp):
    print("A MÉDIA DOS ALUNOS COM NÚMERAÇÃO PAR É MAIOR QUE OS DE NÚMERAÇÃO ÍMPAR")
elif(medImp > medPar):
    print("A MÉDIA DOS ALUNOS COM NÚMERAÇÃO ÍMPAR É MAIOR QUE OS DE NÚMERAÇÃO PAR")
else:
    print("A MÉDIA DOS ALUNOS COM NÚMERAÇÃO PAR É IGUAL AOS DE NÚMERAÇÃO ÍMPAR")