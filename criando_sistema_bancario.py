menu= """


[1]Depositar
[2]Sacar
[3]Extrato
[0]sair


=> """

saldo=0
limite=500
extrato= ""
numero_saques=3
LIMITE_SAQUES=3
while True:

    opcao= input(menu)

    if opcao=="1":
        valor=float(input("Informe o valor do depósito:"))

        if valor>0:
            saldo += valor
            extrato += f"Depósito: R${valor:2f}\n"

        else:

            print("Operação não realizada! O valor informado é invalido.")
            
    
    elif opcao=="2":
       valor= float(input("Informe o valor do Saque:"))
       excedeu_saldo = valor> saldo
       excedeu_limite = valor> limite
       excedeu_saques = numero_saques >= LIMITE_SAQUES

       if excedeu_saldo:
           print("Operação Falhou! Você não tem saldo suficiente")
       elif excedeu_limite:
           print("O valor do saldo excede o limite.")
       elif excedeu_saques:
           print("Numero de saques excedido!")

       elif valor>0:
           saldo -= valor
           extrato+= f"Saque: R${valor:2f}\n"
           numero_saques+=1
       
       else:
           print("Operação falhou! O valor informado é invalido")


    elif opcao=="3":
        print("\n****************************Extrato****************************")
        print("Não existem movimentações" if not extrato else extrato)
        print(f"\nSaldo:R${saldo:2f}")
        print ("********************************")
    elif opcao=="0":
        break
    else: 
        print("Operação invalida, por favor selecione a operação desejada novamente")

