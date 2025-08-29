# ProjetoFinalPython
Projeto final das aulas de Python
Seguindo os seguintes requisitos:
Projeto Integrador Assistente de Desenvolvimento de Aplicativos Computacionais II					
Curso: Técnico em Informática
Turma: INF 13
Professor: Fernando Miguel Oliveira
Datas: Entrega: 26/08	        Recuperação: 28/08	           Apresentação: 02/09

1. Objetivo
O Projeto Integrador tem como objetivo consolidar os conhecimentos adquiridos no módulo de Python/Django, desenvolvendo um sistema web funcional com operações CRUD (Create, Read, Update, Delete). O projeto será realizado em duplas e consiste na criação de um sistema web baseado em um dos temas propostos abaixo. Cada dupla deve implementar um sistema completo, com autenticação de usuários, gerenciamento de pelo menos duas entidades relacionadas, e funcionalidades adicionais como filtros e relatórios.

2. Critérios Obrigatórios
•	Autenticação:
o	Cadastro e login de usuários (administradores e usuários comuns).
o	Uso do sistema de autenticação do Django (Django Authentication)
•	Funcionalidades CRUD:
o	Implementar operações completas (Create, Read, Update, Delete) para as duas entidades principais (ex.: Livros e Empréstimos).
o	Interfaces para listar, criar, editar e excluir registros, com formulários validados.
•	Relacionamentos:
o	As entidades devem ser relacionadas (ex.: um livro pode ter vários empréstimos).
o	Usar chaves estrangeiras no banco de dados para modelar os relacionamentos.

•	Filtros:
o	Implementar pelo menos um filtro de busca (ex.: buscar livros por título ou gênero).
•	Validações:
o	Garantir integridade dos dados com validações no backend (ex.: impedir empréstimos de livros sem estoque ou inscrições duplicadas).
•	Interface:
o	Interface web funcional e responsiva, usando templates Django.
o	Uso de Bootstrap ou CSS básico para estilização.
•	Banco de dados:
o	Modelar as entidades usando Django ORM (models).

3. Temas propostos
As duplas devem escolher um dos seguintes temas para o projeto. Todos os temas possuem o mesmo nível de complexidade e exigem funcionalidades semelhantes. As duplas podem personalizar o contexto do tema (ex.: uma biblioteca de jogos ao invés de livros), desde que mantenham a estrutura de entidades e funcionalidades descritas.
1.	Sistema de Gerenciamento de Biblioteca Escolar
o	Descrição: Sistema para gerenciar uma biblioteca escolar, permitindo o cadastro, consulta, edição e exclusão de livros e empréstimos.
o	Entidades:
	Livros: Título, autor, gênero, ano de publicação, ISBN, quantidade disponível.
	Empréstimos: Aluno, livro, data de empréstimo, data de devolução, status (ativo/devolvido).
o	Funcionalidades: Gerenciamento de livros e empréstimos (CRUD), filtros de busca, relatório de empréstimos pendentes, validação de estoque.



2.	Sistema de Gerenciamento de Cursos Online
o	Descrição: Sistema para gerenciar cursos online, onde administradores cadastram cursos e alunos se inscrevem.
o	Entidades:
	Cursos: Nome, descrição, instrutor, carga horária, categoria.
	Inscrições: Aluno, curso, data de inscrição, status (ativo/concluído).
o	Funcionalidades: Gerenciamento de cursos e inscrições (CRUD), filtros de busca, relatório de alunos inscritos, validação de inscrições duplicadas.
3.	Sistema de Gerenciamento de Tarefas de Projeto
o	Descrição: Sistema para equipes gerenciarem tarefas em projetos, com criação de projetos e atribuição de tarefas.
o	Entidades:
	Projetos: Nome, descrição, data de início, data de término, status (ativo/concluído).
	Tarefas: Título, descrição, responsável (usuário), projeto associado, prazo, status (pendente/em andamento/concluída).
o	Funcionalidades: Gerenciamento de projetos e tarefas (CRUD), filtros de busca, relatório de tarefas pendentes, validação de projetos.
4.	Sistema de Gerenciamento de Estoque de Loja
o	Descrição: Sistema para gerenciar o estoque de uma loja, com cadastro de produtos e registro de entradas/saídas.
o	Entidades:
	Produtos: Nome, descrição, categoria, preço, quantidade em estoque.
	Movimentações: Produto, tipo (entrada/saída), quantidade, data, responsável (usuário).
o	Funcionalidades: Gerenciamento de produtos e movimentações (CRUD), filtros de busca, relatório de estoque baixo, validação de estoque.

4.Tecnologias Obrigatórias
•	Backend: Python com Django (versão mais recente compatível).
•	Frontend: Templates Django com Bootstrap ou CSS básico.
•	Banco de Dados: SQLite (padrão do Django).
•	Controle de Versão: Github

5. Entregas Mínimas 
•	Código-fonte:
o	Projeto Django completo, organizado em apps (ex.: uma app para autenticação, outra para gerenciamento das entidades).
•	Documentação:
o	Descrição das rotas (URLs) do sistema.
o	Instruções para configurar e executar o projeto (ex.: README.md com passos para instalar dependências e rodar o servidor).
•	Apresentação:
o	Demonstração do sistema funcionando (em 02/09).
o	Explicação das funcionalidades implementadas e desafios enfrentados 

6. Prazos e Organização
•	1ª Semana:
o	Configuração do ambiente (Python, Django, banco de dados SQLite/PostgreSQL, repositório Git, templates Django com Bootstrap).
o	Implementação do CRUD da entidade principal (ex.: Livros, Cursos, Projetos ou Produtos) no backend (Django views, models, URLs) e frontend (templates).
o	Configuração da autenticação (Django Authentication com tela de login).

•	2ª Semana:
o	Implementação do CRUD da entidade secundária (ex.: Empréstimos, Inscrições, Tarefas ou Movimentações) no backend e frontend.
o	Implementação da funcionalidade de vinculação (ex.: vincular aluno a curso, tarefa a projeto), com validações de entidades ativas.
o	Aplicação de regras de negócio (ex.: impedir vinculações inválidas) e validações no backend (usando Django Forms).
o	Ajustes de filtros de busca (ex.: busca por nome ou status) e tratamento de erros (ex.: entidade não encontrada).
•	3ª Semana:
o	Integração final entre todos os módulos (autenticação, entidades principais e secundárias).
o	Testes completos do sistema (funcionalidades CRUD, filtros, validações) e correção de erros.
o	Elaboração da documentação (README com descrição, tecnologias, papéis dos integrantes e instruções de execução).
o	Preparação e ensaio da apresentação do projeto.
o	Entrega final

7. Critérios de Avaliação
•	Funcionalidade: Implementação correta das operações CRUD, autenticação, filtros, relatórios e validações.
•	Qualidade do Código: Organização, legibilidade, uso de boas práticas.
•	Interface: Usabilidade, responsividade e design visual.
•	Documentação: Descrição das rotas e instruções de configuração.
•	Apresentação: Clareza na demonstração e explicação do projeto.
