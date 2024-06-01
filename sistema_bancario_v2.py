# Versão 2 do sistema bancário
# Criação do usuário
# Criação da Conta Corrente
def show_menu():
    print("""
_____________________________________________
|                 Y-BANK!                   |   
|___________________________________________|
|              Menu de Opções               |
|                                           |  
| [1] Depositar    [2] Sacar   [3] Extrato  |
|                                           |
| [4] Cad. Cliente    [42] Atualizar Dados  |
| [41] Buscar Cliente [43] Remover Cliente  |
|                                           |
| [5] Criar Conta     [51] Listar Contas    |
|                                           |
| [0] Sair                                  |
|___________________________________________|
""")



def obter_opcao():
    return int(input("> Digite sua opção: "))

def deposito(saldo,extrato,/):
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
        
def saque(*,saldo,extrato,MAX_VALOR,QTDE_SAQUE,cont_saques):
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

def show_extrato(saldo,/,*,extrato):
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

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        print("Você já possui um cadastro conosco.")
    else:
        nome = input("Digite o nome do usuário: ")
        nascimento = input("Digite a data de nascimento do usuário: ")
        endereço = input("Digite o endereço do usuário: ")
        usuarios[cpf] = {
            "nome" : nome,
            "nascimento" : nascimento,
            "cpf" : cpf,
            "endereço" : endereço
        }
        print(f"Cliente {nome} cadastrado com sucesso!")
    return usuarios

def listar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        print(f"Nome: {usuarios[cpf]['nome']}")
        print(f"Data de Nascimento: {usuarios[cpf]['nascimento']}")
        print(f"CPF: {usuarios[cpf]['cpf']}")
        print(f"Endereço: {usuarios[cpf]['endereço']}")
    else:
        print("Usuário não encontrado.")
        
def atualizar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        nome = input("Digite o novo nome do usuário (ou deixe em branco para não alterar): ")
        nascimento = input("Digite a nova data de nascimento do usuário (ou deixe em branco para não alterar): ")
        endereco = input("Digite o novo endereço do usuário (ou deixe em branco para não alterar): ")
        if nome:
            usuarios[cpf]['nome'] = nome
        if nascimento:
            usuarios[cpf]['nascimento'] = (nascimento)
        if endereco:
            usuarios[cpf]['endereco'] = endereco
        print(f"Dados cadastrais do clinte {nome} atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")
    return usuarios
        
def deletar_usuario(usuarios):
    cpf = input("Digite o CPF do cliente: ")
    if cpf in usuarios:
        del usuarios[cpf]
        print("Usuário removido.")
    else:
        print("Usuário não encontrado.")
    return usuarios

def criar_conta(AGENCIA,numero_conta,usuarios):
    cpf = input("Digite o CPF do cliente: ")
    if cpf in usuarios:
        conta = {
            "agencia" : AGENCIA,
            "numero_conta" : numero_conta,
            "usuario" : usuarios[cpf]
        }
        print(f"Conta {numero_conta} criada com sucesso para o cliente {usuarios[cpf]['nome']}.")
        return conta
    else:
        print("Usuário não encontrado.")
    return None

def listar_contas(conta):
    for conta in conta:
        linha = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)

def main():
    QTDE_SAQUE = 3
    MAX_VALOR = 500
    cont_saques = 0        
    saldo = 0
    extrato = ""
    usuarios = {}
    contas = []
    AGENCIA = "0001"
    
    while True:
        show_menu() 
        option = obter_opcao()
        if option == 1:
            saldo,extrato = deposito(saldo,extrato)
        elif option == 2:
            saldo,extrato,cont_saques = saque(saldo,extrato,MAX_VALOR,QTDE_SAQUE,cont_saques)
        elif option == 3:
            show_extrato(saldo,extrato)
        elif option == 4:
            criar_usuario(usuarios)
        elif option == 41:
            listar_usuario(usuarios)
        elif option == 42:
            atualizar_usuario(usuarios)
        elif option == 43:
            deletar_usuario(usuarios) 
        elif option == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif option == 51:
            listar_contas(contas)
        elif option == 0:
            print('\n*** Obrigado por utilizar nossos serviços bancários! ***')
            break
        else:
            print("\n*** Operação inválida, por favor selecione novamente a operação desejada. ***")    
       
main()        

    



    
