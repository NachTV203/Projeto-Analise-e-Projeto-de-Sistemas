# UDF - CENTRO UNIVERSITÁRIO DO DISTRITO FEDERAL

## Ciência da Computação 

**DISCIPLINA – ANÁLISE E PROJETO DE SISTEMAS**  

---

# SISTEMA DE ESTOQUE PARA EVENTOS  
**DOCUMENTAÇÃO DE NEGÓCIOS, REQUISITOS E MODELAGEM UML**

**Alunos:**  
- Beatriz Nevis Miranda - RGM 37227581
- Paulo Andre Gemmal Fonseca - RGM 38030144
- Mauricio Gabriel Gemmal Fonseca - RGM 38031183
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

### Principais Funcionalidades:

Controle de Acesso: Sistema de login para autenticação de usuários, com diferenciação entre administradores e usuários comuns.

Gestão de Estoque: Cadastro, edição, exclusão e consulta de todos os itens disponíveis para locação, com controle de quantidade e valor.

Gestão de Clientes: Manutenção de um cadastro completo dos clientes, incluindo dados de contato e histórico.

Criação de Orçamentos: Ferramenta para selecionar itens do estoque, definir quantidades e gerar um orçamento detalhado para um evento.

Geração de Contratos: Automatização da criação de contratos formais a partir de um orçamento, incluindo dados do cliente, detalhes do evento e lista de itens.

Consulta e Relatórios: Visualização de contratos gerados e potencial para exportação de dados em formatos como PDF e Excel.

### Tecnologias Envolvidas:

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

<img width="2076" height="1155" alt="mermaid-diagram-2025-10-25-190112" src="https://github.com/user-attachments/assets/3d916db4-8fb3-4c89-b188-5f63a24e7cc3" />

O diagrama de sequência UML representa o fluxo completo de execução do sistema de controle de estoque, desde o login do usuário até o encerramento da aplicação. Ele envolve diversos atores e componentes, como o **Usuário**, a **LoginScreen** (tela de autenticação), o banco de dados **users.db** (responsável pelas credenciais), a aplicação principal **EstoqueApp**, o banco **estoque_orcamento.db** (onde ficam os dados de estoque, clientes e contratos) e as **Abas do Sistema**, que compõem a interface modular da aplicação.

Na **fase de autenticação**, o usuário inicia a aplicação e acessa a tela de login. O sistema conecta-se ao banco `users.db`, criando a tabela de usuários e um administrador padrão, caso seja a primeira execução. O usuário insere suas credenciais, que são validadas por meio de hash SHA-256. Se estiverem corretas, as informações são encaminhadas para a aplicação principal.

Durante a **inicialização da aplicação principal**, a tela de login é encerrada e destruída, e o sistema instancia a aplicação **EstoqueApp** com os dados do usuário logado. Em seguida, o sistema conecta-se ao banco `estoque_orcamento.db`, criando ou verificando as tabelas necessárias (estoque, clientes, contratos e contrato_itens).

Na **criação da interface**, o sistema constrói um notebook com abas modulares. Cada aba é criada por uma função específica: Estoque (itens), Clientes (cadastro), Orçamento (pedidos), Contratos (gestão de contratos), Relatórios (visualização de dados) e Configurações (acesso restrito a administradores).

Durante o **carregamento de dados**, o sistema busca informações do banco e preenche as interfaces com as listas de itens, clientes e contratos, exibindo tudo em suas respectivas tabelas (TreeViews).

Na **operação normal**, o usuário interage com as abas, realizando operações de criação, leitura, atualização e exclusão diretamente no banco `estoque_orcamento.db`. As alterações são refletidas em tempo real na interface, com controle de permissões diferenciando administradores de usuários comuns.

Por fim, no **encerramento**, ao fechar a aplicação, o sistema solicita confirmação do usuário. Confirmado o fechamento, as conexões com o banco são encerradas corretamente e a aplicação é finalizada.

O sistema apresenta importantes características: **separação de responsabilidades**, utilizando bancos distintos para autenticação e dados de negócio; **arquitetura modular**, que facilita manutenção e expansão; **segurança**, com senhas armazenadas por hash; **persistência**, com salvamento automático das alterações; e **controle de acesso**, diferenciando as permissões de cada tipo de usuário.



### 6.5 Diagrama de Estado  
 <img width="2076" height="1155" alt="mermaid-diagram-2025-10-20-172154" src="https://github.com/user-attachments/assets/be281312-e18b-4e8b-8ad2-cf1bbf69da08" />

 O diagrama de estados UML do Sistema EletroTec representa o fluxo de navegação e as transições entre os diferentes estados de uma aplicação de controle de estoque e gestão de contratos desenvolvida em Python com Tkinter. O sistema inicia no estado de **Login**, onde o usuário deve se autenticar; em caso de sucesso, é direcionado ao **Dashboard**, ponto central que conecta todos os módulos e para o qual o usuário sempre retorna após concluir qualquer operação. Caso o usuário escolha “Sair”, o sistema é encerrado sem acesso.

O **Dashboard** atua como o núcleo do sistema, possibilitando o acesso aos cinco módulos principais: **Estoque**, **Clientes**, **Orçamento**, **Contratos** e **Relatórios**. No módulo **Estoque**, é possível adicionar, editar ou excluir itens do inventário, sempre com a opção de salvar ou cancelar alterações, retornando à listagem principal. O módulo **Clientes** possui estrutura semelhante, permitindo cadastrar, atualizar ou remover clientes, também seguindo o padrão de operações CRUD (Create, Read, Update, Delete).

O módulo **Orçamento** é o único com fluxo linear e obrigatório, representando o processo de negócio de geração de contratos. O usuário deve selecionar um cliente, preencher os dados do evento, adicionar itens do estoque e, por fim, gerar o contrato, que o direciona automaticamente ao módulo **Contratos**. Neste último, é possível visualizar contratos existentes, alterar seu status (Gerado, Assinado ou Cancelado) e exportá-los em formato PDF, sempre retornando à listagem após cada ação. Já o módulo **Relatórios** é o mais simples, permitindo gerar relatórios de estoque ou contratos e retornando ao estado inicial do módulo após a conclusão.

A navegação é centralizada no Dashboard, com transições bidirecionais entre ele e os demais módulos — permitindo tanto o acesso quanto o retorno. O encerramento completo do sistema ocorre apenas a partir do Dashboard, garantindo que o usuário passe pelo estado central antes de sair. O diagrama destaca ainda a aplicação do padrão CRUD nos módulos de Estoque e Clientes e o fluxo de processo de negócio no módulo Orçamento.

Entre os principais benefícios do diagrama estão a **clareza visual**, que facilita a compreensão do comportamento do sistema; a **manutenibilidade**, útil para desenvolvedores; a **documentação**, que serve como referência técnica; a **validação**, permitindo identificar lacunas nas transições; e a **comunicação**, auxiliando na explicação do funcionamento para stakeholders. Em síntese, o diagrama de estados do Sistema EletroTec reflete uma aplicação bem estruturada, com navegação intuitiva, operações de gestão de dados padronizadas e um fluxo coeso para a geração de contratos. A centralização no Dashboard reforça a consistência da experiência do usuário e facilita futuras expansões do sistema.



### 6.6 Diagrama de Componentes    

#Sistema de Gestão — Estrutura de Componentes#

Este projeto é uma aplicação desktop desenvolvida em Python, utilizando Tkinter e TtkBootstrap para interface gráfica e SQLite como banco de dados.
O sistema gerencia estoque, contratos, clientes e finanças empresariais, sendo modular e fácil de manter.

📁 Estrutura Principal

- main.py → inicializa a aplicação e abre a tela de login.

- login.py (LoginScreen) → autenticação de usuários e acesso ao sistema.

- app_main.py (EstoqueApp) → núcleo principal com interface e controle das abas.

- database.py → conexão e criação do banco SQLite.

- utils.py → funções auxiliares (ícones, locale, formatação e dependências).

- tabs/ → abas modulares: estoque, clientes, orçamentos, contratos, relatórios e configurações.

- financeiro.py (FinanceiroApp) → módulo financeiro independente com gráficos e relatórios.

- setup.py (cx_Freeze) → empacota o projeto em um executável .exe para Windows.

⚙️ Tecnologias Utilizadas

- Python 3

- Tkinter / TtkBootstrap

- SQLite3

- Pandas

- OpenPyXL

- ReportLab

- Matplotlib

- cx_Freeze

🧠 Diagrama de Componentes

O diagrama .drawio/xml incluído no projeto representa as dependências entre módulos e suas interações com bibliotecas externas. Um diagrama de componentes é uma representação visual da estrutura física de um sistema, mostrando seus componentes (como arquivos, bibliotecas, bancos de dados, etc.), suas interfaces e as dependências entre eles.

<img width="910" height="722" alt="Captura de tela 2025-10-19 153501" src="https://github.com/user-attachments/assets/b5be4939-f26c-4f57-9654-349ee053ffcc" />


### 6.7 Diagrama de Objetos  
 
## 🏗️ Análise do Diagrama do Código

O diagrama representa **dois sistemas empresariais integrados** desenvolvidos em Python:

### **1️⃣ Sistema de Estoque e Orçamento (EletroTec)**

#### **Componentes Principais:**

**🔐 LoginScreen (Autenticação)**
- Gerencia login de usuários com senha criptografada (SHA-256)
- Conecta ao banco `users.db`
- Após validação, cria a aplicação principal
- Possui usuário admin padrão (senha: 10092019)

**🖥️ EstoqueApp (Aplicação Principal)**
- Classe central que gerencia toda a interface
- Controla 6 abas diferentes através do componente Notebook
- Mantém conexão com banco de dados SQLite
- Armazena estado da aplicação (orçamento atual, itens selecionados)
- Implementa sistema de checkboxes para seleção múltipla

**📑 Sistema de Abas (Tabs):**
1. **EstoqueTab**: Gerencia inventário de produtos
2. **ClientesTab**: Cadastro e gestão de clientes
3. **OrcamentoTab**: Criação de orçamentos/cotações
4. **ContratosTab**: Geração e acompanhamento de contratos
5. **RelatoriosTab**: Relatórios diversos do sistema
6. **ConfigTab**: Configurações (acesso admin)

**🛠️ Módulos Auxiliares:**
- **DatabaseModule**: Funções para manipulação do banco de dados
- **UtilsModule**: Utilidades gerais (formatação, ícones, validações)

---

### **2️⃣ Sistema Financeiro Empresarial**

#### **Componentes Principais:**

**💰 FinanceiroApp (Dashboard Financeiro)**
- Interface principal com gráficos interativos usando Matplotlib
- Gerencia receitas e despesas
- Usa Pandas DataFrame para análise de dados
- Exporta relatórios formatados para Excel (openpyxl)
- Filtros por ano e mês

**📊 Janelas Secundárias:**

1. **EventosManagerWindow**
   - Gerencia eventos empresariais
   - Lista todos os eventos cadastrados
   - Permite criar, editar e excluir eventos

2. **DividendosWindow**
   - Controla dívidas/dividendos de cada evento
   - Adiciona credores e valores
   - Marca status: "Em Aguardo" ou "Pago"
   - **INTEGRAÇÃO**: Ao marcar como "Pago", registra automaticamente uma despesa no fluxo de caixa

3. **RelatorioMensalWindow**
   - Gera relatórios anuais com resumo mensal
   - Exibe receitas, despesas e saldo por mês
   - Usa código de cores (verde=lucro, vermelho=prejuízo)

4. **TransacaoDialog**
   - Modal para adicionar receitas ou despesas
   - Campos: Data, Descrição/Categoria, Valor
   - Callback para atualizar o sistema após salvar

<img width="7516" height="2756" alt="Untitled diagram-2025-10-20-164707" src="https://github.com/user-attachments/assets/d0e646bc-9f5f-4658-8147-b43e2c334e10" />

---

## 7. Conclusão
A elaboração desta documentação proporcionou uma compreensão aprofundada da estrutura e dos requisitos do Sistema de Estoque para Eventos. O processo de análise do código existente para extrair os requisitos funcionais, não funcionais e regras de negócio foi um exercício prático de engenharia reversa e análise de sistemas.

A modelagem UML foi uma ferramenta crucial para traduzir conceitos abstratos e linhas de código em representações visuais claras e padronizadas. Os diagramas de Caso de Uso e Classe ajudaram a definir o escopo e a estrutura, enquanto os diagramas de Sequência e Atividades permitiram detalhar os fluxos de interação e processos. As principais dificuldades encontradas foram a interpretação de múltiplos arquivos de código, alguns aparentemente não relacionados ao projeto principal, e a necessidade de inferir requisitos não explícitos.

Concluímos que a prática da documentação e modelagem é indispensável para o sucesso de um projeto de software, pois alinha a visão de todos os envolvidos, reduz ambiguidades e cria um guia robusto que orienta o desenvolvimento e a manutenção futura do sistema.  

---

## 8. Referências
BOOCH, G.; RUMBAUGH, J.; JACOBSON, I. UML: guia do usuário. 2. ed. Rio de Janeiro: Campus, 2006.

PRESSMAN, R. S.; MAXIM, B. R. Engenharia de Software: Uma Abordagem Profissional. 8. ed. Porto Alegre: AMGH, 2016.

SOMMERVILLE, I. Engenharia de Software. 10. ed. São Paulo: Pearson Education do Brasil, 2019.

---

## Ficha de Autoavaliação do Grupo  

| Integrantes       | Discussões | Produção escrita | Diagramas UML | Organização | Apresentação |
|-------------------|------------|------------------|---------------|-------------|--------------|
| Beatriz Nevis     |            |                  |               |             |              |
| Paulo Andre       |            |                  |               |             |              |
| Mauricio Gabriel  |            |                  |               |             |              |
| Rafael Junio      |            |                  |               |             |              |
| Victor Alves      |            |                  |               |             |              |

---
