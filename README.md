# 📚 Projeto Biblioteca — Modelagem de Dados e ORM com SQLAlchemy

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

- Python 3.11+
- SQLAlchemy 
- SQLite
- Jupyter Notebook
- Conda / Ambiente virtual
- Git e GitHub

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
## 📂📂 Estrutura atual do Projeto:

project_biblioteca_2/
│
├── notebooks/
│   ├── 01_biblioteca.ipynb
│   ├── 02_modelagens.ipynb
│   └── 03_testes_ORM.ipynb
│
├── src/
│   ├── database/
│   │   ├── base.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── usuario.py
│   │   ├── livro.py
│   │   ├── funcionario.py
│   │   ├── emprestimo.py
│   │   └── item_emprestimo.py
│   │
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   └── create_db.py
│
├── tests/
│   ├── manuais/
│   └── automatizados/
│
├── migrations/
├── logs/
├── wsgi.py
├── pytest.ini
├── requirements.txt
├── LICENSE
└── README.md

## Execução:

Abra o terminal na pasta project_biblioteca_2 e rode:

`python -m create_db`

## 👤 Autor do Projeto:

**Daniel Martins França**

*Projeto desenvolvido com foco em modelagem de dados, bancos de dados relacionais, ORM, testes e evolução para aplicações web.*

## 📬 Contato:

- 📧 Email: [f.daniel.m@gmail.com](mailto:f.daniel.m@gmail.com)  
- 💼 LinkedIn: [www.linkedin.com/in/danixdev](https://www.linkedin.com/in/danixdev)  
- 📁 Trabalhos: [wwww.danixdev.blogspot.com/2026/01/projeto-de-banco-de-dados-para.html](https://danixdev.blogspot.com/2026/01/estruturacao-de-banco-de-dados-para.html)

