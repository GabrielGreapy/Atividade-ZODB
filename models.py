from persistent import Persistent
from persistent.list import PersistentList
from datetime import datetime


class Estoque(Persistent):
    def __init__(self):
        self.estoque = PersistentList()

    def adicionar_Produto(self, nome, validade, estoque):
        data = datetime.now()
        produto = Produto(nome, validade, estoque, data)
        self.estoque.append(produto)
        self._p_changed = 1

    def remover_Produto(self, indice):
        if 0 <= indice < len(self.estoque):
            del self.estoque[indice]
            self._p_changed = 1
        else:
            print("Índice inválido.")


    def listar_Produtos(self):
        if not self.estoque:
            print("Estoque vazio.")
            return

        print("\n Produtos no estoque:")
        for i, produto in enumerate(self.estoque):
            print(f"{i}. {produto.nome} | Validade: {produto.validade} | Quantidade: {produto.estoque}")


class Produto(Persistent):
    def __init__(self, nome, validade, estoque, data):
        self.data = data
        self.nome = nome
        self.validade = validade
        self.estoque = estoque

    def aumentar_Estoque(self, estoque):
        self.estoque += estoque
        self._p_changed = 1

    def diminuir_Estoque(self, estoque):
        self.estoque -= estoque
        self._p_changed = 1

    def checar(self):
        hoje = datetime.now()
        try:
            validade_data = datetime.strptime(self.validade, "%d/%m/%Y")
            dias_restantes = (validade_data - hoje).days
            if dias_restantes <= 8:
                print('O produto está a menos de 8 dias de vencer')
            else:
                print("O produto está a mais de 8 dias para vencer")
        except ValueError:
            print("Formato de data inválido. Use dd/mm/yyyy")
    
class Loja(Persistent):
    def __init__(self):
        self.Carrinhos = PersistentList()
        
    def adicionar_Carrinho(self, novo_Carrinho):
        self.Carrinhos.append(novo_Carrinho)
        self._p_changed = 1 
        print("Item adicionado ao carrinho")

class Carrinhos_Da_Loja(Persistent):
    def __init__(self, carrinho):
        self.carrinho = carrinho
        self.itens_No_Carrinho = PersistentList()
        self._p_changed = 1

    def adicionar_Item_Ao_Carrinho(self, novo_Item):
        self.itens_No_Carrinho.append(novo_Item)
        self._p_changed = 1
        print("Item adicionado ao carrinho")

    def listar_Itens_No_Carrinho(self):
        if not self.itens_No_Carrinho:
            return
        else: 
            for i, item  in enumerate(self.itens_No_Carrinho):
                print(f"{i + 1}: {item}")


    def remove_Item_Ao_Carrinho(self, item):
        if not self.itens_No_Carrinho:
            print("Não há itens no carrinho")
            return
        else:
            del self.itens_No_Carrinho[item]
            self._p_changed = 1
            print("Item deletado")


class Biblioteca(Persistent):
    def __init__(self):
        self.lista_Livros = PersistentList()

    def adicionar_Livro(self, nome):
        livro = Livro(nome)
        self.lista_Livros.append(livro)

class Livro(Persistent):
    def __init__(self, nome):
        self.nome = nome
        self.situacao = "Disponivel"
        
        

    def emprestar(self):
        if self.situacao == "Emprestado":
            print("Livro já está emprestado")
        else:
            self.situacao = "Emprestado"
            self._p_changed = 1

    def devolver(self):
        if self.situacao == "Emprestado":
            self.situacao = "Disponivel"
            self._p_changed = 1
            print("Livro devolvido")
        else: print("O livro já está disponivel")


class Escola(Persistent):
    def __init__(self):
        self.lista_Turma = PersistentList()

    def adicionar_Turma(self, nome):
        turma = Turma(nome)
        self.lista_Turma.append(turma)
        self._p_changed = 1
        print("Turma adicionada")
    
    
class Turma(Persistent):
    def __init__(self, nome):
        self.nome_Turma = nome
        self.lista_Alunos = PersistentList()
    
    def adicionar_Aluno(self, nome):
        aluno = Aluno(nome)
        self.lista_Alunos.append(aluno)
        self._p_changed = 1
        print("Aluno adicionado")


class Aluno(Persistent):
    def __init__(self, nome):
        self.nome_Aluno = nome
        self.presenca = "Indefinido"
    
    def presente(self):
        self.presenca = "Presente"
        self._p_changed = 1
        print("Presente!")

    def faltou(self):
        self.presenca = "Faltou"
        self._p_changed = 1
        print("...Faltou")

        
        
            



    












