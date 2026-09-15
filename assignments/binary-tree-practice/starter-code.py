class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Inserir valor na árvore seguindo a regra da BST
        pass

    def inorder(self, node=None):
        # Retornar valores em ordem: esquerda -> raiz -> direita
        pass

    def preorder(self, node=None):
        # Retornar valores em pré-ordem: raiz -> esquerda -> direita
        pass

    def postorder(self, node=None):
        # Retornar valores em pós-ordem: esquerda -> direita -> raiz
        pass

    def search(self, value):
        # Retornar True se o valor existir na árvore
        pass

    def size(self, node=None):
        # Retornar a quantidade de nós na árvore
        pass


# Exemplo de uso
# tree = BinarySearchTree()
# for value in [8, 3, 10, 1, 6, 14]:
#     tree.insert(value)
# print(tree.inorder())
# print(tree.search(6))
# print(tree.size())
