# 📚 Projeto Biblioteca — Modelagem de Dados e ORM com SQLAlchemy
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Visão Geral

Este projeto tem como objetivo a **modelagem e implementação de um sistema de biblioteca** utilizando **Python**, **SQLAlchemy ORM** e **banco de dados relacional**, com foco em **boas práticas de modelagem**, **organização de código** e **validação conceitual do modelo de dados**.

O sistema contempla entidades como usuários, alunos, professores, livros, empréstimos e itens de empréstimo, incluindo **herança (generalização/especialização)** e **relacionamentos complexos**, alinhados a um DER consistente.

---

## 🎯 Objetivos do Projeto

- Aplicar conceitos de **modelagem conceitual, lógica e física**;
- Implementar **ORM com SQLAlchemy**;
- Utilizar **herança ORM** para representar especializações/generalizações;
- Garantir **integridade referencial** entre entidades;
- Organizar o projeto de forma profissional e escalável;
- Separar claramente **código de domínio**, **testes** e **exploração**.

---

## Diferenciais em Relação a Projetos Anteriores

Este projeto apresenta avanços significativos em relação a implementações anteriores:

### 1. Separação entre código e exploração:

Diferente de projetos anteriores, **o Jupyter Notebook não é usado para criar ou definir tabelas**.  
Ele é utilizado apenas para:
- Documentar decisões de modelagem
- Explorar o mapeamento ORM
- Testar comportamentos e relacionamentos

A definição oficial do banco fica exclusivamente no código Python (`src/`).

---

### 2. Uso consciente do Jupyter Notebook:

O Jupyter é utilizado como:
- Ferramenta de **aprendizado**
- Ambiente de **validação do ORM**
- Suporte à **documentação viva do projeto**

Isso evita:
- Redefinições acidentais de tabelas
- Conflitos de metadata
- Erros comuns em ambientes interativos

---

### 3. Estrutura de projeto profissional
O projeto segue uma organização clara:

- `src/` → códigos de domínio e persistência do bando de dados
- `notebooks/` → modelagem e testes exploratórios (módulo adicional)
- `requirements.txt` → dependências utilizadas
- `README.md` → documentação central

Essa separação facilita:
- Manutenção
- Evolução do sistema
- Migração futura para frameworks web (FastAPI, Django, etc.)

---

## 🔄 Por que o DuckDB foi substituído?

Inicialmente, o projeto utilizou **DuckDB**, porém a escolha foi revista por razões técnicas.

### DuckDB: excelente para análise:

O DuckDB é um banco:
- Colunar
- Extremamente eficiente para **análises analíticas (OLAP)**
- Ideal para ciência de dados e workloads de leitura

Entretanto:

Possui **suporte limitado a restrições relacionais**, como:

- Chaves estrangeiras
- Constraints complexas
- Regras de integridade referencial

Essas limitações impactam diretamente projetos **transacionais (OLTP)**, como sistemas de biblioteca.

---

### 🟢 SQLite: mais adequado ao contexto do projeto

O SQLite foi adotado por ser:

- Um **banco relacional completo**
- Forte em **restrições e integridade**
- Totalmente compatível com SQLAlchemy ORM
- Simples para desenvolvimento local e acadêmico

Para um sistema de biblioteca, onde:

- integridade dos dados é crítica
- relações entre tabelas são fundamentais

O SQLite se mostra **mais apropriado que o DuckDB**.

---

## 🧠 Tecnologias Utilizadas

## Tecnologias Utilizadas

- **Python 3.11+**: linguagem principal do projeto
- **SQLAlchemy ORM**: mapeamento objeto-relacional e manipulação das entidades
- **SQLite**: banco de dados relacional utilizado no desenvolvimento local
- **Pytest**: criação e execução dos testes automatizados
- **Logging**: registro de eventos, validações e erros durante os testes
- **Jupyter Notebook**: documentação exploratória e apoio à modelagem
- **Conda / Ambiente virtual**: gerenciamento do ambiente de desenvolvimento
- **Git e GitHub**: versionamento, branches, releases e pull requests

---

## 📂 Estrutura do Projeto

```
project_biblioteca/
│
├── notebooks/
│   ├── 01_biblioteca.ipynb
│   ├── 02_modelagens.ipynb
│   └── 03_testes_orm.ipynb
│
├── src/
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── aluno.py
│   │   ├── professor.py
│   │   ├── livro.py
│   │   ├── emprestimo.py
│   │   └── item_emprestimo.py
│   │   └── funcionario.py
│   │
│   └── __init__.py
│   └── create_db.py
│   └── model_data_concept_peter_chen.py
│   └── model_data_lofic_james_martin.py
├── .gitignore
├── requirements.txt
└── README.md
```
## Execução:

Abra o terminal na pasta project_biblioteca_2 e rode:

```python -m src.create_db``` 

---

## Evolução Atual do Projeto

Nesta etapa, o projeto evoluiu da modelagem ORM inicial para uma fase de validação prática da camada de dados.

Foram adicionados testes manuais, testes automatizados e logs de execução para garantir que os models, relacionamentos e operações CRUD estejam funcionando corretamente antes da criação da API.

### Banco Oficial

O banco adotado como base oficial do projeto é:

```text
project_biblioteca.db
```

A conexão principal está centralizada em:

```
src/database/connection.py
```

### Testes e Logs:

O projeto agora conta com duas categorias de testes:

```
tests/
├── manuais/
│   ├── test_conexao.py
│   ├── crud_test.py
│   └── crud_emprestimo_test.py
│
└── automatizados/
    ├── conftest.py
    └── test_crud_models.py
```

### Testes Manuais:

Os testes manuais validam diretamente o banco oficial ```project_biblioteca.db.```

Eles foram usados para confirmar:

- conexão com o banco;
- CRUD de Livro;
- CRUD de Usuario;
- CRUD de Funcionario;
- criação de Emprestimo com ItemEmprestimo;
- funcionamento dos logs.
- Testes Automatizados

> Os testes automatizados utilizam pytest e banco SQLite em memória.

Isso permite validar os models sem alterar o banco oficial do projeto.

### Os testes automatizados cobrem:

- configuração dos mapeamentos ORM;
- criação das tabelas esperadas;
- CRUD de Livro;
- CRUD de Usuario;
- CRUD de Funcionario;
- criação de Emprestimo com ItemEmprestimo;
- validação dos relacionamentos principais.
- Executando os Testes

> Para rodar os testes automatizados:

```pytest```

 - Para saída mais detalhada:

```pytest -v```

> Os logs dos testes podem ser exibidos no terminal e salvos em arquivo conforme configuração do pytest.ini.

### Status da Camada ORM:

Nesta versão, a camada ORM foi validada com sucesso para as principais entidades do sistema:

```
Usuario
Aluno
Professor
Funcionario
Livro
Emprestimo
ItemEmprestimo
```

> Também foram validados os principais relacionamentos:

- usuário possui empréstimos;
- funcionário registra empréstimos;
- empréstimo possui itens;
- item de empréstimo referencia um livro.

### Próximos Passos:

A próxima etapa do projeto será a criação de uma API para expor as funcionalidades principais do sistema.

A API deve começar pelos endpoints de Livro:

```
GET    /livros
POST   /livros
GET    /livros/{id_livro}
PUT    /livros/{id_livro}
DELETE /livros/{id_livro}
```
Depois disso, a API será expandida para:

```
usuários;
funcionários;
empréstimos;
itens de empréstimo.
```

### Para verificar a versão atual do projeto:

https://github.com/userdanixdev/project_biblioteca_2/releases/tag/v0.1.0-testes

## 👤 Autor do Projeto:

**Daniel Martins França**

Projeto desenvolvido com foco em modelagem de dados, bancos de dados relacionais e integração com Python, aplicando boas práticas desde a fase conceitual até a implementação utilizando ORM.

## 📬 Contato:

- 📧 Email: [f.daniel.m@gmail.com](mailto:f.daniel.m@gmail.com)  
- 💼 LinkedIn: [www.linkedin.com/in/danixdev](https://www.linkedin.com/in/danixdev)  
- 📁 Trabalhos: [wwww.danixdev.blogspot.com/2026/01/projeto-de-banco-de-dados-para.html](https://danixdev.blogspot.com/2026/01/estruturacao-de-banco-de-dados-para.html)

