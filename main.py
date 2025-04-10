from models import *
import ZODB, ZODB.FileStorage
import transaction

# Abrindo/Conectando com banco ZODB
storage = ZODB.FileStorage.FileStorage('db.fs')
db = ZODB.DB(storage)
conn = db.open()
root = conn.root()

# Inicializa os objetos persistentes se ainda não existirem
if 'estoque' not in root:
    root['estoque'] = Estoque()
if 'loja' not in root:
    root['loja'] = Loja()
if 'biblioteca' not in root:
    root['biblioteca'] = Biblioteca()
if 'escola' not in root:
    root['escola'] = Escola()
    print("✅ Objetos persistentes criados.")

estoque = root['estoque']
loja = root['loja']
biblioteca = root['biblioteca']
escola = root['escola']


def menu_estoque():
    while True:
        print("\n=== MENU ESTOQUE ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Checar validade")
        print("0. Voltar")
        op = input("Escolha uma opção: ")

        if op == '1':
            nome = input("Nome do produto: ")
            validade = input("Data de validade (dd/mm/yyyy): ")
            quantidade = int(input("Quantidade: "))
            estoque.adicionar_Produto(nome, validade, quantidade)
            transaction.commit()
            print(f"✅ Produto '{nome}' adicionado.")
        elif op == '2':
            estoque.listar_Produtos()
            i = int(input("Índice do produto para remover: "))
            estoque.remover_Produto(i)
            transaction.commit()
        elif op == '3':
            estoque.listar_Produtos()
        elif op == '4':
            estoque.listar_Produtos()
            i = int(input("Índice do produto para checar validade: "))
            try:
                estoque.estoque[i].checar()
            except IndexError:
                print("Índice inválido.")
        elif op == '0':
            break
        else:
            print("Opção inválida.")

def menu_loja():
    while True:
        print("\n=== MENU LOJA ===")
        print("1. Criar novo carrinho")
        print("2. Adicionar item ao carrinho")
        print("3. Listar itens do carrinho")
        print("4. Remover item do carrinho")
        print("0. Voltar")
        op = input("Escolha uma opção: ")

        if op == '1':
            novo = Carrinhos_Da_Loja("Carrinho")
            loja.adicionar_Carrinho(novo)
            transaction.commit()
        elif op == '2':
            if not loja.Carrinhos:
                print("Nenhum carrinho criado.")
                continue
            item = input("Item a adicionar: ")
            loja.Carrinhos[-1].adicionar_Item_Ao_Carrinho(item)
            transaction.commit()
        elif op == '3':
            if loja.Carrinhos:
                loja.Carrinhos[-1].listar_Itens_No_Carrinho()
            else:
                print("Nenhum carrinho criado.")
        elif op == '4':
            if loja.Carrinhos:
                loja.Carrinhos[-1].listar_Itens_No_Carrinho()
                i = int(input("Índice do item para remover: ")) - 1
                loja.Carrinhos[-1].remove_Item_Ao_Carrinho(i)
                transaction.commit()
            else:
                print("Nenhum carrinho criado.")
        elif op == '0':
            break
        else:
            print("Opção inválida.")

def menu_biblioteca():
    while True:
        print("\n=== MENU BIBLIOTECA ===")
        print("1. Adicionar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Listar livros")
        print("0. Voltar")
        op = input("Escolha uma opção: ")

        if op == '1':
            nome = input("Nome do livro: ")
            biblioteca.adicionar_Livro(nome)
            transaction.commit()
        elif op == '2':
            for i, livro in enumerate(biblioteca.lista_Livros):
                print(f"{i}. {livro.nome} - {livro.situacao}")
            i = int(input("Índice do livro: "))
            biblioteca.lista_Livros[i].emprestar()
            transaction.commit()
        elif op == '3':
            for i, livro in enumerate(biblioteca.lista_Livros):
                print(f"{i}. {livro.nome} - {livro.situacao}")
            i = int(input("Índice do livro: "))
            biblioteca.lista_Livros[i].devolver()
            transaction.commit()
        elif op == '4':
            for i, livro in enumerate(biblioteca.lista_Livros):
                print(f"{i}. {livro.nome} - {livro.situacao}")
        elif op == '0':
            break
        else:
            print("Opção inválida.")

def menu_escola():
    while True:
        print("\n=== MENU ESCOLA ===")
        print("1. Criar turma")
        print("2. Adicionar aluno à turma")
        print("3. Marcar presença")
        print("4. Listar alunos")
        print("0. Voltar")
        op = input("Escolha uma opção: ")

        if op == '1':
            nome = input("Nome da turma: ")
            escola.adicionar_Turma(nome)
            transaction.commit()
        elif op == '2':
            for i, turma in enumerate(escola.lista_Turma):
                print(f"{i}. {turma.nome_Turma}")
            i = int(input("Índice da turma: "))
            nome_aluno = input("Nome do aluno: ")
            escola.lista_Turma[i].adicionar_Aluno(nome_aluno)
            transaction.commit()
        elif op == '3':
            for i, turma in enumerate(escola.lista_Turma):
                print(f"{i}. {turma.nome_Turma}")
            i = int(input("Índice da turma: "))
            turma = escola.lista_Turma[i]
            for j, aluno in enumerate(turma.lista_Alunos):
                print(f"{j}. {aluno.nome_Aluno} - {aluno.presenca}")
            j = int(input("Índice do aluno: "))
            status = input("Presente (p) ou Faltou (f)? ").lower()
            if status == 'p':
                turma.lista_Alunos[j].presente()
            else:
                turma.lista_Alunos[j].faltou()
            transaction.commit()
        elif op == '4':
            for i, turma in enumerate(escola.lista_Turma):
                print(f"\nTurma: {turma.nome_Turma}")
                for aluno in turma.lista_Alunos:
                    print(f"- {aluno.nome_Aluno} ({aluno.presenca})")
        elif op == '0':
            break
        else:
            print("Opção inválida.")


while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Estoque")
    print("2. Loja")
    print("3. Biblioteca")
    print("4. Escola")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        menu_estoque()
    elif opcao == '2':
        menu_loja()
    elif opcao == '3':
        menu_biblioteca()
    elif opcao == '4':
        menu_escola()
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")


conn.close()
db.close()
