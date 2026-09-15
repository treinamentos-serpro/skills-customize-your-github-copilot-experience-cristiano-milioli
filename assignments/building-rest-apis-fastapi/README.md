# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST simples em Python com FastAPI para praticar rotas, validação de dados, manipulação de recursos e testes básicos de endpoints.

## 📝 Tarefas

### 🛠️ Configurar a aplicação FastAPI

#### Descrição
Crie a estrutura inicial da API, configure a aplicação principal e defina um modelo de dados para representar tarefas.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` com título e versão da aplicação.
- Definir uma lista em memória para armazenar tarefas.
- Criar um modelo de dados usando `BaseModel` com campos como `id`, `title` e `done`.
- Garantir que a aplicação possa ser iniciada com um comando como `uvicorn app:app --reload`.

### 🛠️ Implementar endpoints de leitura

#### Descrição
Adicione rotas para listar todas as tarefas e consultar uma tarefa específica por identificador.

#### Requisitos
O programa concluída deve:

- Expor um endpoint `GET /tasks` para retornar todas as tarefas.
- Expor um endpoint `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Retornar erro `404` quando a tarefa não existir.
- Usar respostas em formato JSON.

### 🛠️ Criar operações de escrita

#### Descrição
Implemente a criação, atualização e remoção de tarefas para completar o ciclo CRUD da API.

#### Requisitos
O programa concluído deve:

- Expor um endpoint `POST /tasks` para criar uma nova tarefa.
- Expor um endpoint `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Expor um endpoint `DELETE /tasks/{task_id}` para remover uma tarefa.
- Validar entradas e manter o estado em memória durante a execução da aplicação.

### 🛠️ Testar a API

#### Descrição
Verifique o comportamento da API com chamadas HTTP para confirmar que os endpoints respondem corretamente.

#### Requisitos
O programa concluído deve:

- Enviar requisições para todos os endpoints principais.
- Confirmar respostas de sucesso para criação, leitura e atualização.
- Confirmar erro ao acessar uma tarefa inexistente.
- Documentar pelo menos dois exemplos de requisição e resposta.
