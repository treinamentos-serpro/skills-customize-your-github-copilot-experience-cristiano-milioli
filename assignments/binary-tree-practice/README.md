# 📘 Atividade: Binary Tree Practice

## 🎯 Objetivo

Explorar o conceito de árvore binária em Python, incluindo criação de nós, inserção de valores e travessias em ordem para praticar estruturas de dados e lógica recursiva.

## 📝 Tarefas

### 🛠️ Definir a estrutura da árvore

#### Descrição
Crie a classe `Node` e a estrutura básica de uma árvore binária com referência para os filhos esquerdo e direito.

#### Requisitos
O programa concluído deve:

- Definir uma classe `Node` com atributos para `value`, `left` e `right`.
- Permitir a criação de nós com valores numéricos.
- Iniciar uma árvore vazia e depois inserir nós manualmente.

### 🛠️ Inserir valores na árvore

#### Descrição
Implemente a lógica de inserção em uma árvore binária de busca, seguindo a regra de menor à esquerda e maior à direita.

#### Requisitos
O programa concluído deve:

- Criar uma classe `BinarySearchTree` com método `insert`.
- Inserir valores seguindo a regra da árvore binária de busca.
- Aceitar múltiplos valores em sequência.
- Garantir que valores duplicados sejam tratadas de forma clara.

### 🛠️ Percorrer a árvore

#### Descrição
Implemente diferentes formas de percorrer a árvore para visualizar os valores armazenados.

#### Requisitos
O programa concluído deve:

- Implementar travessia em ordem (`inorder`).
- Implementar travessia pré-ordem (`preorder`).
- Implementar travessia pós-ordem (`postorder`).
- Exibir os resultados de cada travessia em sequência.

### 🛠️ Buscar e validar dados

#### Descrição
Adicione operações para verificar se um valor existe na árvore e para contar quantos nós ela possui.

#### Requisitos
O programa concluído deve:

- Implementar um método `search(value)` que retorne `True` ou `False`.
- Implementar um método `size()` para contar todos os nós da árvore.
- Validar cenários com árvore vazia e com valores ausentes.
- Exibir mensagens claras quando um valor for encontrado ou não.
