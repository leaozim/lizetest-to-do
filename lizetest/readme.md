Bem-vindo ao nosso desafio para a vaga de Desenvolvedor Python/Django FullStack! Este é um teste projetado para avaliar suas habilidades e conhecimentos técnicos. Antes de começar, certifique-se de configurar o ambiente de desenvolvimento conforme as instruções abaixo.

# Configuração do Ambiente

1. Crie um virtualenv
2. Instale as dependências do projeto
3. Migre o banco de dados
4. Rode o projeto

# Desafios

Desafio 1 - Verificação de Senha no Frontend
Na tela de cadastro de usuário (/accounts/singup/), adicione uma verificação via JavaScript no frontend para fornecer feedback em tempo real ao usuário, indicando se as senhas coincidem.

Desafio 2 - Redirecionamento para a Tela de Login
Ao acessar as telas de listagem, cadastro e edição de uma task (/, task/create/, task/int:pk/delete/), redirecione  para a tela de login caso o usuário não esteja autenticado.

Desafio 3 - Redirecionamento após login
Após a autenticação do usuário (/accounts/login/), o sistema deverá redirecionar para a listagem de tasks.

Desafio 4 - Herança
Herde as características do modelo BaseModel no app "core" no modelo Category no app "todo"

Desafio 5 - CRUD do Modelo "Category"
No app "todo", implemente as operações CRUD (listagem, cadastro, edição e exclusão) para o modelo "Category". Adicione o campo "category" no formulário de cadastro da Task (task/create/).

Desafio 6 - Filtro de Tasks por Usuário Autenticado
Na listagem de Tasks, filtre apenas as tarefas criadas pelo usuário autenticado. Ou seja, um usuário X não deve visualizar as tarefas criadas pelo usuário Y.

Desafio 7 - Rota de API (use Django Rest Framework) para Marcar uma Task como "Completa"
Crie uma rota de API para marcar uma Task como "Completa". Na listagem de tasks, implemente um checkbox que, ao ser clicado, envia uma requisição ao backend marcando a task como completada. Se desmarcar, a mesma rota deve ser chamada para desfazer a marcação.

Desafio 8 - Bloqueio para Remover Task Completada
Impedir a remoção de uma task marcada como completada a nível de backend, não apenas no frontend.

Desafio 9 - Redesign nas Telas
Aplique um redesign nas telas do sistema utilizando o template Bootstrap disponível em https://adminlte.io/. Baixe os HTMLs do template e integre-os ao projeto, utilizando conceitos como templates, blocks e includes. Crie um sidebar com duas opções: categorias e tasks.

Desafio 10 - Adição de Testes Unitários
Implemente testes unitários para pelo menos duas funcionalidades a sua escolha no projeto.

# Entrega do Projeto

1. Crie um repositório privado em seu GitHub.
2. Envie suas modificações para o projeto no GitHub.
3. Adicione o usuário franklindias como colaborador do projeto.
4. Marque a data desejada para a apresentação do projeto em https://calendar.app.google/moy5AsStjGd8vJTB6

Sinta-se à vontade para adicionar ou aprimorar funcionalidades, bem como melhorar as implementações existentes conforme julgar apropriado. Boa sorte!