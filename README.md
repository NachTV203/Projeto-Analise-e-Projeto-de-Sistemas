# UDF - CENTRO UNIVERSITÁRIO DO DISTRITO FEDERAL

## Ciência da Computação 

**DISCIPLINA – ANÁLISE E PROJETO DE SISTEMAS**  

---

# SISTEMA DE ESTOQUE PARA EVENTOS  
**DOCUMENTAÇÃO DE NEGÓCIOS, REQUISITOS E MODELAGEM UML**

**Alunos:**  
- Beatriz Nevis Miranda - RGM 37227581
- Nome Completo - RGM  
- Nome Completo - RGM  
- Rafael Junio Azevedo Souza - RGM 38595435
- Victor Alves Moreira - RGM 30159067

**Professor:** Gabriel de Oliveira Alves  

Brasília – 2025.10  

---

## Sumário
1. Introdução  
2. Justificativa  
3. Objetivos  
   - 3.1 Objetivo Geral  
   - 3.2 Objetivos Específicos  
4. Descrição do Sistema Proposto  
5. Requisitos  
   - 5.1 Requisitos Funcionais  
   - 5.2 Requisitos Não Funcionais  
   - 5.3 Regras de Negócio  
6. Diagramas UML  
   - 6.1 Diagrama de Casos de Uso  
   - 6.2 Diagrama de Classe  
   - 6.3 Diagrama de Atividades  
   - 6.4 Diagrama de Sequência  
   - 6.5 Diagrama de Estado  
   - 6.6 Diagrama de Componentes  
   - 6.7 Diagrama de Objetos  
7. Conclusão  
8. Referências  

---

## 1. Introdução
O presente trabalho detalha a análise e o projeto de um Sistema de Estoque para Eventos, desenvolvido como parte da disciplina de Análise e Projeto de Sistemas. O projeto visa atender às necessidades de empresas de locação de materiais para eventos, um mercado que demanda agilidade e controle preciso sobre seus ativos. O sistema proposto, chamado EletroTec, é uma aplicação de desktop que centraliza a gestão de inventário, clientes, orçamentos e a geração de contratos.
A documentação de requisitos e a modelagem UML (Unified Modeling Language) são pilares fundamentais no ciclo de vida do desenvolvimento de software. Elas garantem que as necessidades do cliente sejam claramente compreendidas e traduzidas em uma estrutura de sistema coesa e funcional. Através desta documentação, estabelecemos uma base sólida para a construção, testes e manutenção do software, facilitando a comunicação entre os stakeholders e a equipe de desenvolvimento e assegurando que o produto final atenda aos objetivos propostos.

---

## 2. Justificativa
Empresas que atuam no ramo de locação de equipamentos para eventos frequentemente enfrentam desafios operacionais significativos. A falta de um sistema integrado resulta em controles manuais, geralmente em planilhas, que são suscetíveis a erros, dificultam o acesso rápido à informação e não oferecem uma visão clara da disponibilidade dos itens. Isso pode levar a problemas como overbooking de equipamentos, perda de material, dificuldades na elaboração de orçamentos e morosidade na geração de contratos.
O Sistema de Estoque para Eventos é importante porque resolve esses problemas ao automatizar e centralizar as operações essenciais. Ele oferece um controle rigoroso sobre o inventário, agiliza a criação de orçamentos e contratos, e mantém um cadastro organizado de clientes. O impacto esperado é um aumento significativo na eficiência operacional, redução de perdas financeiras por falhas de gestão, melhoria na qualidade do serviço prestado ao cliente e uma tomada de decisão mais assertiva, baseada em dados concretos. 

---

## 3. Objetivos  

### 3.1 Objetivo Geral  
Desenvolver a documentação de negócios, requisitos e modelagem UML de um sistema de gestão de estoque para eventos, a fim de criar uma base clara e estruturada para seu desenvolvimento e implementação.  

### 3.2 Objetivos Específicos  
Identificar e descrever os requisitos funcionais e não funcionais do sistema EletroTec.
Elaborar os principais diagramas UML para representar as diferentes visões do sistema (casos de uso, classes, sequência, etc.).
Produzir uma documentação de negócios e requisitos que sirva como guia para a equipe de desenvolvimento.
Aplicar metodologias de elicitação e análise de requisitos para garantir que o escopo do sistema atenda às necessidades do negócio.
---

## 4. Descrição do Sistema Proposto
O sistema proposto é uma aplicação de desktop desenvolvida em Python com a biblioteca Tkinter para a interface gráfica e SQLite para o armazenamento de dados.
Público-alvo: O sistema destina-se aos funcionários de empresas de locação de materiais para eventos, abrangendo desde os gestores de estoque até a equipe comercial responsável pela elaboração de orçamentos e contratos.
Principais Funcionalidades:
Controle de Acesso: Sistema de login para autenticação de usuários, com diferenciação entre administradores e usuários comuns.
Gestão de Estoque: Cadastro, edição, exclusão e consulta de todos os itens disponíveis para locação, com controle de quantidade e valor.
Gestão de Clientes: Manutenção de um cadastro completo dos clientes, incluindo dados de contato e histórico.
Criação de Orçamentos: Ferramenta para selecionar itens do estoque, definir quantidades e gerar um orçamento detalhado para um evento.
Geração de Contratos: Automatização da criação de contratos formais a partir de um orçamento, incluindo dados do cliente, detalhes do evento e lista de itens.
Consulta e Relatórios: Visualização de contratos gerados e potencial para exportação de dados em formatos como PDF e Excel.
Tecnologias Envolvidas:
Linguagem: Python 3
Interface Gráfica (GUI): Tkinter
Banco de Dados: SQLite 3
Bibliotecas Adicionais: reportlab (para geração de PDF), openpyxl (para exportação para Excel).

---

## 5. Requisitos  

### 5.1 Requisitos Funcionais  
Exemplo:  
- **RF01 – Cadastro de Cliente**: O sistema deve permitir o cadastro de clientes, incluindo nome completo, CPF, endereço, telefone e e-mail.  

### 5.2 Requisitos Não Funcionais  
Exemplo:  
- **RNF01 – Desempenho**: O sistema deve responder às solicitações em até 2 segundos.  

### 5.3 Regras de Negócio  
Exemplo:  
- O cliente só pode ser cadastrado se informar CPF válido e não estiver previamente registrado no sistema.  

---

## 6. Diagramas UML  

### 6.1 Casos de Uso  
Resumo e descrição dos casos de uso.  
Inserir diagramas aqui.  

### 6.2 Diagrama de Classe  
Resumo e imagem do diagrama.  

### 6.3 Diagrama de Atividades  
Resumo e imagem do diagrama.  

### 6.4 Diagrama de Sequência  
Resumo e imagem do diagrama.  

### 6.5 Diagrama de Estado  
Resumo e imagem do diagrama.  

### 6.6 Diagrama de Componentes  
Resumo e imagem do diagrama.  

### 6.7 Diagrama de Objetos  
Resumo e imagem do diagrama.  

---

## 7. Conclusão
*Resumo sobre a experiência: aprendizados, dificuldades e contribuições da modelagem.*  

---

## 8. Referências
*Inserir as referências em formato ABNT.*  

---

## Ficha de Autoavaliação do Grupo  

| Integrantes       | Discussões | Produção escrita | Diagramas UML | Organização | Apresentação |
|-------------------|------------|------------------|---------------|-------------|--------------|
| Nome Completo 01  |            |                  |               |             |              |
| Nome Completo 02  |            |                  |               |             |              |
| Nome Completo 03  |            |                  |               |             |              |
| Nome Completo 04  |            |                  |               |             |              |

---
