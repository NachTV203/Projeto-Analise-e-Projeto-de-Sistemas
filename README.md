# 📦 EletroTec - Sistema de Gestão de Estoque para Eventos

![Status](https://img.shields.io/badge/Status-Documenta%C3%A7%C3%A3o%20e%20Modelagem-blue)
![Linguagem](https://img.shields.io/badge/Linguagem-Python%203-yellow)
![GUI](https://img.shields.io/badge/GUI-Tkinter%20%2F%20TtkBootstrap-orange)
![DB](https://img.shields.io/badge/Banco%20de%20Dados-SQLite-lightgrey)

Este repositório contém a documentação de negócios, levantamento de requisitos e modelagem UML do sistema **EletroTec**, desenvolvido para a disciplina de **Análise e Projeto de Sistemas** no **Centro Universitário do Distrito Federal (UDF)**.

---

## 👥 Equipe de Desenvolvimento

| Nome do Aluno | RGM |
| :--- | :--- |
| **Beatriz Nevis Miranda** | 37227581 |
| **Paulo Andre Gemmal Fonseca** | 38030144 |
| **Mauricio Gabriel Gemmal Fonseca** | 38031183 |
| **Rafael Junio Azevedo Souza** | 38595435 |
| **Víctor Alves Moreira** | 30159067 |

**Orientador:** Prof. Gabriel de Oliveira Alves

---

## 📝 Visão Geral do Projeto

O **EletroTec** é uma aplicação desktop projetada para empresas de locação de materiais para eventos. O objetivo é substituir controles manuais e planilhas por um sistema centralizado que gerencia inventário, clientes, orçamentos e gera contratos automaticamente em PDF.

### 🎯 Objetivos
- **Geral:** Criar uma base estruturada (requisitos e UML) para o desenvolvimento do sistema.
- **Específicos:** 
  - Automatizar a geração de orçamentos e contratos.
  - Garantir o controle rigoroso de disponibilidade de equipamentos.
  - Fornecer relatórios financeiros e de estoque em tempo real.

---

## 🛠️ Tecnologias e Arquitetura

O sistema utiliza uma arquitetura modular dividindo responsabilidades entre interface, lógica de negócio e persistência.

- **Linguagem:** Python 3.10+
- **Interface Gráfica:** Tkinter com tema TtkBootstrap.
- **Persistência:** SQLite 3 (Bancos independentes: `users.db`, `estoque.db`, `financeiro.db`).
- **Processamento de Dados:** Pandas.
- **Geração de Documentos:** ReportLab (PDF) e OpenPyXL (Excel).

---

## 📋 Requisitos do Sistema

### Requisitos Funcionais (Principais)
| ID | Nome | Descrição |
| :--- | :--- | :--- |
| **RF01** | Autenticação | Login seguro com diferenciação entre Admin e Usuário Padrão. |
| **RF02** | Gestão de Estoque | CRUD completo de itens com cálculo automático de valor total. |
| **RF03** | Gestão de Clientes | Cadastro e histórico de locações de clientes. |
| **RF04** | Orçamentos | Seleção de múltiplos itens para cotação de eventos. |
| **RF05** | Contratos | Conversão de orçamentos em contratos PDF com status (*Gerado/Assinado*). |
| **RF06** | Financeiro | Dashboard com fluxo de caixa, dívidas e dividendos. |

### Requisitos Não Funcionais
- **Segurança:** Senhas criptografadas via hash **SHA-256**.
- **Desempenho:** Resposta das consultas ao banco em menos de **3 segundos**.
- **Portabilidade:** Empacotamento via `cx_Freeze` para execução em Windows (.exe).

---

## 📊 Modelagem UML

O projeto foi totalmente modelado utilizando a linguagem UML para garantir que a implementação siga as regras de negócio.

### 🖼️ Diagramas Implementados:
- [x] **Casos de Uso:** Interação dos atores com o sistema.
- [x] **Diagrama de Classes:** Estrutura das entidades (Produto, Cliente, Contrato).
- [x] **Diagrama de Sequência:** Fluxo de dados entre login e módulos principais.
- [x] **Diagrama de Estados:** Ciclo de vida da aplicação e dos contratos.
- [x] **Diagrama de Componentes:** Organização modular dos arquivos `.py` e bibliotecas.
- [x] **Diagrama de Objetos:** Instâncias em tempo de execução (Budgets e DataFrames).

> *Os diagramas podem ser encontrados na pasta `/docs/diagrams` deste repositório.*

---

## 🚀 Estrutura de Pastas

```bash
├── main.py            # Ponto de entrada do sistema
├── login.py           # Módulo de autenticação
├── app_main.py        # Núcleo da interface (Notebook/Tabs)
├── database.py        # Conexão e comandos SQLite
├── tabs/              # Abas modulares (estoque, clientes, orçamentos...)
├── financeiro.py      # Dashboard e lógica financeira
├── utils.py           # Formatação e utilitários
└── assets/            # Ícones e imagens
