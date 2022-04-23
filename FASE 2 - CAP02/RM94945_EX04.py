#4- Ao analisar o código do programa deles, porém, você descobre que a senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.
password = int(input("Digite o minutos marcado nesse momento para descobrirmos a senha: "))

i = int(0)
fat = int(1)

if(password >= 60 or password < 0):
    print("minuto inexistente")
else:
    for i in range(i, password):
            fat = fat * (password - i)
    
print("A SENHA É: LIBERDADE{}".format(fat))