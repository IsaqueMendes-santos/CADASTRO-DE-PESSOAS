import os
opcao = 0
codigo_produtos = []
nome_produtos = []
preco_produtos = []
quantidades = []

while (opcao != 3):
    print("------ MENU -----")
    print("1 - para cadastrar")
    print("2 - para listar")
    print("3 - para excluir produto")
    print("4 - para sair")

    opcao = int(input("escolha a opção: "))
    
    
    if opcao == 1:
     codigo_produto = float(input("digite o codigo do produto que deseja"))
     nome_produto = float(input("Digite o nome do produto"))  
     preco_produto = float(input("preco do produto"))
     quantidade = float(input("Fale a quantidade do produto"))

     arquivo = open("cad_pessoas.txt", "a")
     arquivo.write(f"{nome_produto},{codigo_produto},{preco_produto},{quantidade}\n")
     arquivo.close()
     print("cadastrar produto")

    elif (opcao == 2):
        print("listar pessoas")

        arquivo = open("cad_pessoas.txt", "r")
        
        for linha in arquivo:
            nome_produto,codigo_produto,preco_produto,quantidade = linha.strip().split(" ,")
            print(f"nome do produto:  {nome_produto}")
            print(f"Telefone da pessoa:  {codigo_produto}")
            print(f"Email da pessoa:  {preco_produto}")
            print(f"Email da pessoa:  {quantidade}")
            print("-----------------------------------------")
        arquivo.close()
      
        input()
        os.system("cls")
    
    elif (opcao == 3):
       arquivo.open("produtos.txt", "r")
       linhas = arquivo.readlines()
       arquivo.close()

       remover = int(input("digite a linha que deseja remover"))
       remover = remover - 1
       linhas.pop(remover)

       arquivo = open ("produtos.txt", "w")
       for linha in linhas:
          arquivo.write(linha)
       arquivo.close()

    print("produto removido com sucesso!!!")
    input()
    os.system("cls")