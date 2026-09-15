# 📘 Atividade: Task Manager em Python

## 🎯 Objetivo

Construir um pequeno gerenciador de tarefas em Python para praticar listas, dicionários, funções, entrada e saída de dados e persistência em arquivo.

## 📝 Tarefas

### 🛠️ Criar o menu principal

#### Descrição
Implemente um menu interativo para que o usuário possa adicionar, listar, marcar e remover tarefas.

#### Requisitos
O programa concluído deve:

- Exibir um menu com opções como adicionar, listar, concluir e remover tarefa.
- Receber entrada do usuário para escolher uma ação.
- Manter o programa em execução até o usuário sair.
- Usar funções separadas para cada operação do menu.

### 🛠️ Gerenciar as tarefas

#### Descrição
Crie a estrutura de dados para armazenar tarefas e organize a lógica para manipular cada item do gerenciador.

#### Requisitos
O programa concluído deve:

- Armazenar tarefas em uma lista de dicionários.
- Cada tarefa deve conter pelo menos um identificador, um título e um status de concluído.
- Permitir adicionar novas tarefas com nome e descrição curta.
- Permitir marcar uma tarefa como concluída.
- Permitir remover uma tarefa pelo seu identificador.

### 🛠️ Persistir os dados em arquivo

#### Descrição
Salve as tarefas em um arquivo local para que elas continuem disponíveis mesmo após fechar o programa.

#### Requisitos
O programa concluído deve:

- Ler as tarefas existentes no início da execução.
- Salvar as tarefas em um arquivo como JSON ou TXT.
- Atualizar o arquivo sempre que uma tarefa for adicionada, removida ou concluída.
- Garantir que o programa não quebre se o arquivo ainda não existir.

### 🛠️ Validar e melhorar a experiência

#### Descrição
Finalize a aplicação com melhorias de usabilidade, validação simples e mensagens claras para o usuário.

#### Requisitos
O programa concluído deve:

- Validar entradas do usuário antes de processá-las.
- Exibir mensagens amigáveis para ações bem-sucedidas ou erros.
- Organizar a saída para mostrar tarefas com status como “pendente” ou “concluída”.
- Incluir uma opção para sair do programa de forma limpa.
