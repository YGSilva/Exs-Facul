#1- Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
print("-----TIPOS DE ASSINATURA-----")
print("BASIC \nSILVER \nGOLD \nPLATINIUM")
ass = str(input("\nTipo de assinatura do cliente:"))
fat = float(input("Faturamento anual: R$ "))

if str.upper(ass) == "BASIC":
    desc = 0.3
elif str.upper(ass) == "SILVER":
    desc = 0.2
elif str.upper(ass) == "GOLD":
    desc = 0.1
elif str.upper(ass) == "PLATINIUM":
    desc = 0.05
else:
    print("ASSINATURA INEXISTENTE")

bonus = float(fat * desc)

print("\nVALOR DO BÔNUS A SER RECEBIDO DO CLIENT: R$ {}".format(round(bonus, 2)))