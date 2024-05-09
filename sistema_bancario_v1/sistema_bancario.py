#sistema bancario simples v1.0
LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500.00

saldo_conta = 0.0
valor_depositado = [] 
saque_realizado = []
numero_de_saques = 0
opcao = None

menu = '''
    | Banco do Povo |

[d] para depositar um valor 
[s] para sacar um valor
[e] para exibir extrato
[q] para sair

=> '''

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite o valor a depositar: "))
        valor_depositado.append(valor_deposito)
        saldo_conta += valor_deposito
        print("\nValor depositado")
    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))
        
        if saque > saldo_conta: 
            print(f"\nSaldo insuficiente para o saque de R${saque}")
        elif saque >= VALOR_LIMITE_SAQUE:
            print("\nValor superior ao limite de saque\nSomente saques inferiores a R$ 500,00 são suportados")
        elif numero_de_saques >= LIMITE_SAQUE:
            print("\nNumero de saques diários excedido\nTente novamente amanhã!")
        else: 
            saldo_conta -= saque
            saque_realizado.append(saque)
            numero_de_saques += 1
            print("\nValor sacado!")
    
    elif opcao == "e":
        print("    EXTRATO DAS OPERAÇÕES:    ")  
        print("Depositos: ")
        for i in valor_depositado: 
            print(f"R${i}")
        print("Saques: ")
        for j in saque_realizado:
            print(f"R${j}")  
        print(f"Saldo atual: R${saldo_conta}") 
            
    elif opcao == "q":
        break 

    else: 
        print("Opção incorreta\nTente novamente!")    
    