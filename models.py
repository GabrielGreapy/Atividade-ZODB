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
        x = self.data - hoje
        if x.total_seconds() <= 691200: 
            print('O produto está a menos de 8 dias perto de vencer')
        else: print("O produto está a mais de 8 dias para vencer")

    
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
            for i,  in enumerate(self.itens_No_Carrinho):
                print(f"{i + 1}: {self.itens_No_Carrinho[i]}")


    def remove_Item_Ao_Carrinho(self, item):
        if not self.itens_No_Carrinho:
            print("Não há itens no carrinho")
            return
        else:
            del self.item_No_Carrinho(item)
            self._p_changed = 1
            print("Item deletado")

        
        
            



    












