
#MENU 
menu = """
************************************
*            DIO BANKS             *
************************************

> Selecione uma Opção:

[d] Deposito
[s] Saque
[e] Extrato
[x] Sair

=> """  

saldo = 0
extrato=''
LIMITE_SAQUES=500
SAQUES_DIA=3
cont_saques=0

while True:
    opcao = input(menu)

    if opcao=='d':
        valor = float(input(">> Digite o valor do Depósito: "))
        if valor > 0:
            print(f">> Deposito de R$ {valor:.2f} realizado!")
            saldo+=valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print(">> Você digitou um valor negativo ou zero. Tente novamente")            
    elif opcao=='s':
        
        valor = float(input(">> Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_SAQUES

        excedeu_saques = cont_saques >= SAQUES_DIA

        if excedeu_saldo:
            print(">> Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(">> Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print(">> Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            cont_saques += 1
        else:
            print(">> Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "x":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        