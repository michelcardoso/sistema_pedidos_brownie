def boas_vindas():
    print("Bem-vindo ao Sistema de Pedidos de Brownie!")
    print("Escolha uma opção no menu")

def menu():
    print("1. Fazer Cadastro")
    print("2. Fazer pedido")
    print("3. Ver Histórico")
    print("0. Sair")

def sair():
    print("Até mais e volte sempre !!!")

boas_vindas()
menu()
opcao = int(input("Digite o numero da opção desejada:"))
if opcao == 1:
    print("Fazer cadastro")
elif opcao ==2:
    print("Fazer pedido")
elif opcao ==3:
    print("Ver historico")
elif opcao ==0:
    sair()
else:
    print("Opção inválida. Tente novamente")
