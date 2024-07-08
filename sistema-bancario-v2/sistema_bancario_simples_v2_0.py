import textwrap
import tkinter
#sistema bancario simples v2.0
def depositar(saldo_conta, valor_inserido, extrato):
    if valor_inserido > 0:
        saldo_conta += valor_inserido  
        extrato += f"Depósito:\tR${valor_inserido:2.f}\n"
    else: 
        print("\n@@@ Operacao falhou! @@@")

    return saldo_conta, extrato
    
def sacar(*, saldo_conta, valor, quantia_limite, extrato, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    quantia_limite_excedida = valor >= quantia_limite
    limite_saque_excedido = numero_de_saques >= limite_saques
    
    if saldo_excedido: 
        print("\n@@@ Erro na operação! Saldo insuficiente. @@@")
    elif quantia_limite_excedida:
        print("\n@@@ Erro na operação! Quantia limite excedida! @@@")
    elif limite_saque_excedido:
        print("\n@@@ Erro na operação! Limite de saques excedidos! @@@")

    elif valor > 0:
        saldo_conta -= valor
        extrato += f"Saque:\tR$ {valor:2.f}\n"
        numero_de_saques += 1
        print("\n----- Saque realizado com sucesso! -----")
    else:
        print("@@@ Erro na operação! Valor inválido. @@@")

    return saldo_conta, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhum registro para extrato encontrado" if not extrato else extrato)
    print(f"Saldo:\t\t{saldo:2.f}\n")
    print("\n=============================")

def filtro_de_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Digite o cpf do usuário")
    usuario = filtro_de_usuario(usuarios, cpf)

    if usuario: 
        print("\n@@@ Já existe um usuário com este cpf @@@")
        return
    
    nome = input("Informe o nome completo:")
    data_de_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa):")
    endereco = input("Informe o endereço completo(logradouro, Nro-bairro-cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco})
    print("==== Usuario criado com êxito ====")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário:")
    usuario = filtro_de_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com êxito ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else: 
        print("\n@@@ Usuário não encontrado. Processo de criação de conta interrompido! @@@")

def listar_contas(contas):
        for conta in contas:
            linha = f"""
                Agencia:\t{conta["agencia"]}
                C/C:\t\t{conta["numero_conta"]}
                Titular:{conta["usuario"]}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

LIMITE_SAQUES = 3
AGENCIA = "0001"

valor_limite_saque = 500.00
saldo_conta = 0.0
valor_deposito = 0.0 

numero_de_saques = 0

opcao = None
extrato = ""

contas = []
usuarios = []


menu = '''
    | Banco do Povo |

[d] para depositar um valor 
[s] para sacar um valor
[u] para criar novo usuário
[n] para criar nova conta
[l] para listar contas 
[e] para exibir extrato
[q] para sair

=> '''

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite o valor a depositar: "))
        saldo, extrato = depositar(saldo_conta, valor_deposito, )

    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))
        saldo, extrato = sacar(
                    saldo_conta=saldo_conta, 
                    valor=saque, 
                    quantia_limite=valor_limite_saque, 
                    extrato=extrato, 
                    numero_saques=numero_de_saques, 
                    limite_saques=LIMITE_SAQUES
                    )
            
    elif opcao == "e":
        exibir_extrato(saldo_conta, extrato=extrato) 
            
    elif opcao == "u":
        criar_usuario(usuarios)
    
    elif opcao == "n":
        numero_conta = len(contas) + 1
        nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if nova_conta:
            contas.append[nova_conta]
    elif opcao == "l":
        if not contas:
            print("\nNão há contas cadastradas!")
        else:
            listar_contas(contas)
    elif opcao == "q":
        break 

    else: 
        print("Opção incorreta\nTente novamente!")    
    