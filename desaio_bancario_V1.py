menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor >= 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Deposito no valor de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("Operação falhou! Valor inválido para deposito.")

    elif opcao == "s":     
        print(f"Limite diário de saques: {LIMITE_SAQUES - numero_saques}")

        if numero_saques == LIMITE_SAQUES:
            print("Operação falou! Limite de saques diários atingido")
        else:
            valor = float(input("Informe o valor do saque: "))
            if valor >= limite:
                print("Operação falhou! Limite de saque atingido")
            else:
                if valor >= saldo:
                    print("Operação falou! Saldo insuficiente para saque")
                else:
                    if valor > 0:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}"
                        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
                        numero_saques += 1
                    else:
                        print("Operação falhou! Valor inválido para saque.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")