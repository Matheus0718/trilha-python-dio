
operacao = int(input("""Escolha uma opcao:
                    [1] Depósito
                    [2] Saque
                    [3] Extrato 
                    [4] sair  """))
saldo = 0
limite_n_saques =3
limite = 500
n_saques=0
while operacao != 4:
     if operacao == 1:
        deposito = float(input("Digite o valor do depósito "))
        if deposito > 0:
          saldo = saldo + deposito  
          print("Os saldo atual é de R$ {}".format(saldo))
        else:
         print("Valor incorreto")
         quit()

     elif operacao ==2:
               saque = float(input("Digite o valor do saque "))
               excedeu_saldo = saque > saldo
               excedeu_saques = n_saques >= limite_n_saques
               excedeu_limite = saque > limite
               if excedeu_saldo:
                print("Operação falhou, voce nao tem saldo")
               elif excedeu_limite:
                print("Operação falhou, voce nao tem limite")
               elif excedeu_saques:
                   print("Operação falhou, numero de saques excedidoo")
               elif saque > 0:
                  saldo = saldo - saque
                  print("O saldo depois do saque é {}".format(saldo))
                  n_saques = n_saques +1
               else:
                  print("Valor invalido")
                  quit()
     elif operacao == 3:
       print("====================EXTRATO============\n    o seu saldo é de R$ :{}".format(saldo))
       quit()
     else:
        print("Opção invalida, selecione a operação desejada")
