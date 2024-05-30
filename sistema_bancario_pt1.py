# o sistema bancario precisa de 3 operações: sacar-depositar-extrato
# Função Depósito
# Aceita somente valores > 0
# Deve ser colocado no extrato o valor do depósito

def show_menu():
    print("""
___________________
|     YBANK!      |   
|_________________|
| Menu de Opções  |
|                 | 
| [d] Depositar   |
| [s] Sacar       |
| [e] Extrato     |
| [q] Sair        |
|_________________|
""")


def obter_opcao():
    return input("> Digite sua opção: ").lower()

def deposito(saldo,extrato):
    try:
        valor = float(input("\n> Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"> Você depositou: R$ {valor:.2f}\n"
            print('\n*** Operação realizada com sucesso! ***')
        else:
            print("\n*** O valor do depósito precisa ser maior que R$ 0.00 ***")
    except ValueError:
        print("\n*** Operação falhou! O valor informado é inválido. ***")
    
    return saldo,extrato
        
def saque(saldo,extrato,MAX_VALOR,QTDE_SAQUE,cont_saques):
    try:
        valor = float(input("\n> Informe o valor do saque: "))
        if valor > saldo:
            print("\n*** Saldo Insuficiente ***")
            print(f'\n*** Saldo Atual: R$ {saldo:.2f} ***')
        elif valor > MAX_VALOR:
            print(f'\n*** O valor máximo por saque é de: R${MAX_VALOR:.2f} ***')
        elif cont_saques >= QTDE_SAQUE:
            print('\n*** Você excedeu a quantidade de saque diária. Volte amanhã! ***')
        elif valor > 0:
            saldo -= valor
            extrato += f'> Você sacou: R$ {valor:.2f}\n'
            cont_saques += 1 
            print('\n*** Operação realizada com sucesso! ***')
        else:
            print("\n*** Operação falhou! O valor informado é inválido. ***")
    except ValueError:
        print("\n*** Operação falhou! O valor informado é inválido. ***")  
    
    return saldo,extrato, cont_saques   

def show_extrato(saldo,extrato):
    if not extrato:
        print("=====================================")
        print(" Nenhuma movimentação foi realizada. ")
        print("=====================================")

    else:
        print("============================")
        print("      Extrato Bancário      ")
        print("============================")
        print(extrato) 
        print(f'Saldo: R$ {saldo:.2f}')
        print("============================")

def main():
    QTDE_SAQUE = 3
    MAX_VALOR = 500
    cont_saques = 0        
    saldo = 0
    extrato = ""
    
    while True:
        show_menu() 
        option = obter_opcao()
        if option == 'd':
            saldo,extrato = deposito(saldo,extrato)
        elif option == 's':
            saldo,extrato,cont_saques = saque(saldo,extrato,MAX_VALOR,QTDE_SAQUE,cont_saques)
        elif option == 'e':
            show_extrato(saldo,extrato)
        elif option == 'q':
            print('\n*** Obrigado por utilizar nossos serviços bancários! ***')
            break
        else:
            print("\n*** Operação inválida, por favor selecione novamente a operação desejada. ***")    
       
main()        

    



    