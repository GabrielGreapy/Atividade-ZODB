from models import *
import ZODB, ZODB.FileStorage
import transaction

# Abrindo/Conectando com banco ZODB
storage = ZODB.FileStorage.FileStorage('db.fs')
db = ZODB.DB(storage)
conn = db.open()
root = conn.root()

# Cria o estoque se ainda não tiver
if 'estoque' not in root:
    root['estoque'] = Estoque()
    print("✅ Estoque inicial criado.")

estoque = root['estoque']

# Menu simples
while True:
    print("\n==== Menu ====")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Checar validade do produto")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        validade = input("Data de validade: ")
        quantidade = int(input("Quantidade: "))
        estoque.adicionar_Produto(nome, validade, quantidade)
        transaction.commit()
        print(f"✅ Produto '{nome}' adicionado.")
    
    elif opcao == '2':
        print("\n Produtos no estoque:")
        Estoque.listar_Produtos()

    elif opcao == '3':
        Estoque.listar_Produtos()
        produto = input("Qual produto você quer checar validade?")



    
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")

# Fechar conexão
conn.close()
db.close()
