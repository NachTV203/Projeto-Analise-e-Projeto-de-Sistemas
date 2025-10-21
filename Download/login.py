# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib
import os
import sys
import traceback

# Importa funções e classes necessárias de outros módulos
from utils import set_window_icon, APP_VERSION, COMPANY_NAME # Importa de utils.py
from app_main import EstoqueApp                     # Importa de app_main.py
import database                                      # Importa database.py

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Estoque EletroTec")
        self.root.geometry("350x250")
        self.root.resizable(False, False)
        # Usa a função center_toplevel adaptada para a janela raiz
        self.center_window()
        set_window_icon(self.root, "Invento+.ico")
        self.user_db_conn = None
        self.user_db_cursor = None
        self.setup_user_db()
        self.create_widgets()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def setup_user_db(self):
        """Configura ou conecta ao banco de dados de usuários."""
        db_path = database.get_db_path("users.db") # Usa função de database.py
        print(f"Conectando ao banco de dados de usuários em: {db_path}")
        try:
            self.user_db_conn = sqlite3.connect(db_path)
            self.user_db_cursor = self.user_db_conn.cursor()
            self.user_db_cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL, full_name TEXT, is_admin INTEGER DEFAULT 0,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP)
            """)
            self.user_db_cursor.execute("SELECT COUNT(*) FROM users WHERE is_admin = 1")
            if self.user_db_cursor.fetchone()[0] == 0:
                default_password = "10092019"
                hashed_password = hashlib.sha256(default_password.encode()).hexdigest()
                self.user_db_cursor.execute("INSERT INTO users (username, password, full_name, is_admin) VALUES (?, ?, ?, ?)",
                                    ("admin", hashed_password, "Administrador", 1))
                self.user_db_conn.commit()
                print(f"Usuário 'admin' criado com senha padrão: {default_password}")
        except sqlite3.Error as e:
            messagebox.showerror("Erro Crítico de Banco de Dados", f"Não foi possível configurar o banco de usuários ({db_path}): {e}\n\nA aplicação será encerrada.", parent=self.root if self.root.winfo_exists() else None)
            if self.root: self.root.quit()
        except Exception as e:
             messagebox.showerror("Erro Crítico Inesperado", f"Erro ao configurar DB de usuários:\n{e}\n{traceback.format_exc()}\n\nA aplicação será encerrada.", parent=self.root if self.root.winfo_exists() else None)
             if self.root: self.root.quit()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill='both', expand=True)
        ttk.Label(main_frame, text="Controle de Estoque", font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        ttk.Label(main_frame, text="Usuário:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entry_username = ttk.Entry(main_frame, width=25)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)
        self.entry_username.focus()
        ttk.Label(main_frame, text="Senha:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.entry_password = ttk.Entry(main_frame, width=25, show="•")
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))
        btn_login = ttk.Button(btn_frame, text="Entrar", command=self.attempt_login, width=15)
        btn_login.pack(side=tk.LEFT, padx=5)
        btn_cancel = ttk.Button(btn_frame, text="Sair", command=self.quit_login, width=15)
        btn_cancel.pack(side=tk.LEFT, padx=5)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=3)
        self.root.bind('<Return>', lambda event: self.attempt_login())
        self.entry_password.bind('<Return>', lambda event: self.attempt_login())

    def attempt_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        if not username or not password:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha usuário e senha!", parent=self.root)
            return
        if not self.user_db_conn or not self.user_db_cursor:
             messagebox.showerror("Erro Interno", "Conexão com banco de dados de usuários não está ativa.", parent=self.root)
             return
        try:
            self.user_db_cursor.execute("SELECT password, full_name, is_admin FROM users WHERE username = ?", (username,))
            result = self.user_db_cursor.fetchone()
            login_successful = False
            if result:
                stored_password_hash = result[0]
                input_password_hash = hashlib.sha256(password.encode()).hexdigest()
                if stored_password_hash == input_password_hash:
                    login_successful = True
                    user_info = {'username': username, 'full_name': result[1], 'is_admin': bool(result[2])} # Cria dict com info do user

            if login_successful:
                self.close_user_db_connection() # Fecha DB de usuários
                self.root.destroy()           # Fecha janela de login
                self.launch_main_app(user_info) # Passa user_info para a app principal
            else:
                messagebox.showerror("Login Falhou", "Usuário ou senha incorretos!", parent=self.root)
                self.entry_password.delete(0, 'end')
                self.entry_password.focus()
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Não foi possível verificar as credenciais: {e}", parent=self.root)
        except Exception as e:
             messagebox.showerror("Erro Inesperado no Login", f"Ocorreu um erro: {e}\n{traceback.format_exc()}", parent=self.root)

    def launch_main_app(self, user_info):
        """Inicia a janela principal da aplicação."""
        main_root = tk.Tk()
        app = EstoqueApp(main_root, user_info) # Cria instância da app principal
        main_root.mainloop()

    def close_user_db_connection(self):
        """Fecha a conexão com o banco de dados de usuários."""
        # Usa a função close_db do módulo database
        self.user_db_conn, self.user_db_cursor = database.close_db(self.user_db_conn, "users.db")

    def quit_login(self):
        """Fecha a conexão do DB de usuários e encerra a aplicação."""
        self.close_user_db_connection()
        self.root.quit()
