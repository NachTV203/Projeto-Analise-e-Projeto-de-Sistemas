# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import traceback
from datetime import datetime

# Importações de módulos customizados
import database
from utils import (APP_VERSION, COMPANY_NAME, set_window_icon, check_dependencies,
                   REPORTLAB_AVAILABLE, getSampleStyleSheet)

# Importações das funções que criam e populam cada aba
# ATENÇÃO: Vamos precisar importar as funções de atualização de botões também
from tabs.estoque_tab import (criar_aba_estoque, carregar_dados_estoque,
                              ordenar_coluna, atualizar_botoes_estoque) # <- Adicionado atualizar_botoes_estoque
from tabs.clientes_tab import (criar_aba_clientes, carregar_dados_clientes,
                               atualizar_botoes_cliente) # <- Adicionado atualizar_botoes_cliente
from tabs.orcamento_tab import criar_aba_orcamento, filtrar_itens_orcamento
from tabs.contratos_tab import (criar_aba_contratos, carregar_dados_contratos,
                                atualizar_botoes_contrato) # <- Adicionado atualizar_botoes_contrato
from tabs.relatorios_tab import criar_aba_relatorios
from tabs.config_tab import criar_aba_configuracoes

class EstoqueApp:
    def __init__(self, root, user_info):
        self.root = root
        self.user_info = user_info # Armazena as informações do usuário logado
        self.root.title(f"EletroTec v{APP_VERSION} - {COMPANY_NAME}")
        self.root.geometry("1320x880")
        set_window_icon(self.root, "Invento+.ico")

        # Aplica tema (opcional)
        try:
            style = ttk.Style(root)
            available_themes = style.theme_names()
            # Dando preferência a temas mais modernos se disponíveis
            if 'clam' in available_themes: style.theme_use('clam')
            elif 'vista' in available_themes: style.theme_use('vista')
            elif 'xpnative' in available_themes: style.theme_use('xpnative')
            else: style.theme_use('default') # Fallback
            print(f"Temas disponíveis: {available_themes}. Usando: {style.theme_use()}")
        except tk.TclError as e:
            print(f"Erro ao aplicar tema: {e}")
            pass # Continua sem tema customizado

        # Verifica dependências opcionais (ReportLab, Openpyxl)
        check_dependencies(self.root)

        # Conecta ao banco de dados principal e cria tabelas
        self.conn, self.cursor = database.connect_db()
        if self.conn and self.cursor:
            database.create_tables(self.cursor, self.conn)
        else:
            # Se a conexão falhou em database.connect_db, ele já mostrou erro e saiu.
            # Mas por segurança, verificamos aqui também.
            messagebox.showerror("Erro Crítico", "Falha na conexão com o banco de dados principal. A aplicação será encerrada.", parent=self.root if self.root.winfo_exists() else None)
            if self.root: self.root.quit()
            return # Impede o resto da inicialização se DB falhar

        # --- Inicialização de atributos de estado ---
        # Usados para armazenar dados temporários ou estado da UI entre funções/abas
        self.orcamento_atual = []               # Lista de dicts para itens na aba Locação/Contrato
        self.cliente_id_edicao_atual = None     # Guarda o ID do cliente sendo editado na aba Clientes
        self._ordem_atual_estoque = {}          # Guarda a última coluna/direção ordenada na tree Estoque
        self._ordem_atual_clientes = {}         # Guarda a última coluna/direção ordenada na tree Clientes
        self._ordem_atual_contratos = {}        # Guarda a última coluna/direção ordenada na tree Contratos

        # --- NOVOS DICIONÁRIOS PARA RASTREAR CHECKBOXES ---
        self.checked_items_estoque = {}     # {item_db_id: True/False}
        self.checked_items_clientes = {}    # {cliente_id: True/False}
        self.checked_items_contratos = {}   # {contract_id: True/False}
        # ---------------------------------------------------

        # Estilos para PDF (ReportLab)
        if REPORTLAB_AVAILABLE:
            try:
                self.estilos_pdf = getSampleStyleSheet()
                # TODO: Adicionar estilos customizados aqui se necessário (ex: para títulos, tabelas)
            except Exception as e:
                print(f"Erro ao carregar estilos PDF: {e}")
                self.estilos_pdf = None # Fallback
        else:
            self.estilos_pdf = None

        # --- Criação da Interface Gráfica Principal ---
        self.criar_interface_principal()

        # --- Criação das Abas (delegando para os módulos) ---
        # Cada função `criar_aba_*` recebe `self` (a instância da app principal)
        # para que possa acessar/modificar atributos da app (ex: self.notebook, self.conn)
        # e adicionar os widgets da aba ao `self.notebook`.
        criar_aba_estoque(self)
        criar_aba_clientes(self)
        criar_aba_orcamento(self)
        criar_aba_contratos(self)
        criar_aba_relatorios(self)
        criar_aba_configuracoes(self) # <<< Agora sempre criada, a lógica de admin fica DENTRO dela

        # --- Carregamento inicial dos dados nas abas ---
        # Chama as funções que populam as Treeviews iniciais
        try:
            carregar_dados_estoque(self)    # Popula a lista de estoque
            carregar_dados_clientes(self)   # Popula a lista de clientes
            filtrar_itens_orcamento(self)   # Popula o combobox de itens na aba Orçamento
            carregar_dados_contratos(self)  # Popula a lista de contratos gerados
        except Exception as e:
            # Mostra um erro genérico se qualquer carregamento inicial falhar
            messagebox.showerror("Erro ao Carregar Dados Iniciais",
                                 f"Ocorreu um erro ao carregar os dados iniciais:\n{e}\n\n{traceback.format_exc()}",
                                 parent=self.root)
            # A aplicação continua, mas pode estar com dados faltando

        # Define ação ao fechar a janela (botão [X])
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def criar_interface_principal(self):
        """Cria os elementos base da interface: Notebook e Status Bar."""
        # Notebook (container para as abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=(5,0)) # padding(N,S,L,O) ou (X, Y) ou (all)

        # Barra de Status
        # Mostra o nome completo se disponível, senão o username. Indica se é admin.
        user_display_name = self.user_info.get('full_name') or self.user_info.get('username', 'N/A')
        admin_status = " (Admin)" if self.user_info.get('is_admin', False) else ""
        status_text = f"Usuário: {user_display_name}{admin_status} | Status: Conectado"
        self.status_bar = ttk.Label(self.root, text=status_text, relief=tk.SUNKEN, anchor=tk.W, padding=(5,2))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def on_closing(self):
        """Função chamada ao tentar fechar a janela principal."""
        # Pergunta ao usuário se realmente quer sair
        if messagebox.askokcancel("Sair", "Deseja realmente sair do EletroTec?", icon='question', parent=self.root):
            print("Encerrando aplicação...")
            # Fecha a conexão com o banco de dados ANTES de destruir a janela
            # Verifica se self.conn existe e não é None (caso a conexão inicial tenha falhado)
            if hasattr(self, 'conn') and self.conn:
                self.conn, self.cursor = database.close_db(self.conn)
            # Destroi a janela principal do Tkinter, encerrando o mainloop
            self.root.destroy()

# O código principal que inicia a aplicação está em main.py
# Este arquivo (app_main.py) define a classe principal da aplicação,
# mas não a executa diretamente se importado como módulo.