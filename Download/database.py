# -*- coding: utf-8 -*-
import sqlite3
import os
import sys
import traceback
from tkinter import messagebox # Para erros críticos de conexão

def get_db_path(db_name="estoque_orcamento.db"):
    """Retorna o caminho completo para o arquivo do banco de dados."""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__)) # Assume que database.py está na raiz
    return os.path.join(base_path, db_name)

def connect_db(db_name="estoque_orcamento.db"):
    """Conecta ao banco de dados especificado e retorna a conexão e o cursor."""
    db_path = get_db_path(db_name)
    print(f"Conectando ao banco de dados em: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        conn.text_factory = str
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        print(f"Conexão com {db_name} estabelecida.")
        return conn, cursor
    except sqlite3.Error as e:
        messagebox.showerror("Erro Crítico de Banco de Dados",
                             f"Não foi possível conectar ao banco de dados principal '{db_path}':\n{e}\n\nA aplicação será encerrada.")
        sys.exit(1) # Encerra a aplicação se não conseguir conectar ao DB principal
    except Exception as e:
        messagebox.showerror("Erro Crítico Inesperado",
                             f"Erro inesperado ao conectar ao banco de dados '{db_path}':\n{e}\n{traceback.format_exc()}\n\nA aplicação será encerrada.")
        sys.exit(1)

def create_tables(cursor, conn):
    """Cria as tabelas do banco de dados principal se não existirem."""
    try:
        # Tabela Estoque
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE COLLATE NOCASE,
                quantidade INTEGER NOT NULL, valor_unitario REAL NOT NULL, valor_total REAL NOT NULL,
                data_atualizacao TEXT NOT NULL)
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_estoque_nome ON estoque (nome)")

        # Tabela Clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cliente_id INTEGER PRIMARY KEY AUTOINCREMENT, nome_razao TEXT NOT NULL UNIQUE COLLATE NOCASE,
                endereco TEXT, cnpj_cpf TEXT, contato TEXT, observacoes TEXT,
                data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP)
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_clientes_nome ON clientes (nome_razao COLLATE NOCASE)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_clientes_cnpj ON clientes (cnpj_cpf COLLATE NOCASE)")

        # Tabela Contratos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contratos (
                contract_id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_nome TEXT NOT NULL,
                cliente_endereco TEXT, cliente_cnpj TEXT, cliente_contato TEXT,
                evento_nome TEXT NOT NULL, evento_local TEXT NOT NULL, data_inicio_evento TEXT NOT NULL,
                data_fim_evento TEXT NOT NULL, prazo_locacao TEXT NOT NULL, valor_contrato REAL NOT NULL,
                data_geracao TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Gerado' CHECK(status IN ('Gerado', 'Assinado', 'Cancelado')))
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contratos_cliente ON contratos (cliente_nome COLLATE NOCASE)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contratos_evento ON contratos (evento_nome COLLATE NOCASE)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contratos_data ON contratos (data_geracao)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contratos_status ON contratos (status)")

        # Tabela Contrato Itens
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contrato_itens (
                contrato_item_id INTEGER PRIMARY KEY AUTOINCREMENT, contract_id INTEGER NOT NULL,
                item_nome TEXT NOT NULL COLLATE NOCASE, quantidade INTEGER NOT NULL,
                valor_unitario_ref REAL NOT NULL, valor_total_ref REAL NOT NULL,
                FOREIGN KEY (contract_id) REFERENCES contratos (contract_id) ON DELETE CASCADE)
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contrato_itens_contract ON contrato_itens (contract_id)")

        conn.commit()
        print("Tabelas do banco de dados principal verificadas/criadas.")
    except sqlite3.Error as e:
        messagebox.showerror("Erro ao Criar Tabelas", f"Não foi possível criar/verificar as tabelas:\n{e}")
        conn.rollback() # Desfaz alterações se houver erro
    except Exception as e:
        messagebox.showerror("Erro Inesperado", f"Erro inesperado ao criar tabelas:\n{e}\n{traceback.format_exc()}")
        conn.rollback()

def close_db(conn, db_name="estoque_orcamento.db"):
    """Fecha a conexão com o banco de dados."""
    if conn:
        try:
            conn.close()
            print(f"Conexão com {db_name} fechada.")
            return None, None # Retorna None para conn e cursor
        except Exception as e:
            print(f"Erro ao fechar conexão {db_name}: {e}")
    return conn, None # Retorna a conexão (que pode já ser None) e None para cursor
