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

## 3.2 Objetivos Específicos  

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

RF01 – Autenticação de Usuários: O sistema deve permitir que usuários acessem o sistema através de um nome de usuário e senha.
RF02 – Controle de Nível de Acesso: O sistema deve diferenciar usuários "Administradores" de usuários "Padrão", limitando o acesso a certas funcionalidades (como a aba de configurações).
RF03 – Gerenciar Itens de Estoque: O sistema deve permitir cadastrar, consultar, editar e excluir itens do estoque. Os dados mínimos são: nome, quantidade, valor unitário e valor total.
RF04 – Gerenciar Clientes: O sistema deve permitir cadastrar, consultar, editar e excluir clientes. Os dados mínimos são: nome/razão social, endereço, CNPJ/CPF e contato.
RF05 – Criar Orçamento: O sistema deve permitir que um usuário selecione itens do estoque e suas quantidades para compor um orçamento.
RF06 – Gerar Contrato: O sistema deve permitir a geração de um contrato a partir de um orçamento, associando-o a um cliente e adicionando informações do evento (nome, local, datas).
RF07 – Consultar Contratos: O sistema deve permitir a visualização e busca de contratos já gerados.
RF08 – Gerenciar Usuários (Admin): O sistema deve permitir que um usuário administrador crie, edite e remova outros usuários (funcionalidade implícita pela existência do campo is_admin no banco de dados de usuários).
RF09 – Exclusão de Contrato em Cascata: Ao excluir um contrato, o sistema deve excluir automaticamente todos os itens associados a ele.
5.2 Requisitos Não Funcionais
RNF01 – Desempenho: As consultas ao banco de dados e o carregamento das listas (estoque, clientes) devem ser concluídos em até 3 segundos.
RNF02 – Segurança: As senhas dos usuários devem ser armazenadas no banco de dados de forma criptografada (hash).
RNF03 – Usabilidade: A interface do sistema deve ser intuitiva, seguindo os padrões de aplicações de desktop, para que um usuário com conhecimentos básicos de informática possa operá-lo.
RNF04 – Confiabilidade: O sistema deve utilizar um banco de dados persistente (SQLite) para garantir que os dados não sejam perdidos ao fechar a aplicação.
RNF05 – Portabilidade: A aplicação deve ser executável em sistemas operacionais Windows (versão 7 ou superior).
5.3 Regras de Negócio
RN01: Um item de estoque deve possuir um nome único no sistema.
RN02: Um cliente deve possuir um nome/razão social único no sistema.
RN03: Um usuário deve possuir um nome de usuário (username) único no sistema.
RN04: O sistema deve garantir a existência de pelo menos um usuário administrador. Caso nenhum exista, um usuário "admin" padrão deve ser criado.
RN05: Um contrato só pode ser gerado se estiver associado a um cliente cadastrado.
RN06: O valor total de um item de estoque é calculado automaticamente (quantidade * valor unitário).
RN07: Um contrato possui um status que pode ser 'Gerado', 'Assinado' ou 'Cancelado'.

### 5.2 Requisitos Não Funcionais  
RNF01 – Desempenho: As consultas ao banco de dados e o carregamento das listas (estoque, clientes) devem ser concluídos em até 3 segundos.
RNF02 – Segurança: As senhas dos usuários devem ser armazenadas no banco de dados de forma criptografada (hash).
RNF03 – Usabilidade: A interface do sistema deve ser intuitiva, seguindo os padrões de aplicações de desktop, para que um usuário com conhecimentos básicos de informática possa operá-lo.
RNF04 – Confiabilidade: O sistema deve utilizar um banco de dados persistente (SQLite) para garantir que os dados não sejam perdidos ao fechar a aplicação.
RNF05 – Portabilidade: A aplicação deve ser executável em sistemas operacionais Windows (versão 7 ou superior).  

### 5.3 Regras de Negócio  
RN01: Um item de estoque deve possuir um nome único no sistema.
RN02: Um cliente deve possuir um nome/razão social único no sistema.
RN03: Um usuário deve possuir um nome de usuário (username) único no sistema.
RN04: O sistema deve garantir a existência de pelo menos um usuário administrador. Caso nenhum exista, um usuário "admin" padrão deve ser criado.
RN05: Um contrato só pode ser gerado se estiver associado a um cliente cadastrado.
RN06: O valor total de um item de estoque é calculado automaticamente (quantidade * valor unitário).
RN07: Um contrato possui um status que pode ser 'Gerado', 'Assinado' ou 'Cancelado'.

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
