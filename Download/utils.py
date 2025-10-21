# -*- coding: utf-8 -*-
import locale
import os
import sys
import tkinter as tk
from tkinter import messagebox # Importar messagebox aqui
from datetime import datetime

# --- Constantes de Informação do Software ---
APP_VERSION = "Beta 1.6"
UPDATE_DATE = "17/04/2025"
COMPANY_NAME = "IMAGEM"
COMPANY_CNPJ = "00.578.278/0001-40"
COMPANY_ADDRESS = "SAAN QR 1 LOTE 175"
CONTRACT_CITY = "Brasília"

# Tenta importar dependências opcionais e define flags
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, KeepTogether
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch, cm
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


# --- Configuração de Locale ---
def setup_locale():
    """Configura o locale para pt_BR, com fallbacks."""
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_ALL, 'Portuguese')
            except locale.Error:
                try:
                    locale.setlocale(locale.LC_ALL, '') # Locale padrão do sistema
                    print(f"Atenção: Locale Português não encontrado. Usando locale padrão: {locale.getlocale()}.")
                except locale.Error:
                     print(f"Atenção: Não foi possível definir nenhum locale. Usando locale 'C'.")


# --- Funções Auxiliares ---
def format_currency(value):
    """Formata um valor numérico como moeda brasileira (R$)."""
    if value is None: value = 0.0
    try:
        f_value = float(str(value).replace(',', '.'))
        return locale.currency(f_value, grouping=True, symbol='R$')
    except (ValueError, TypeError, locale.Error):
        return "R$ Inválido"

def unformat_currency(value_str):
    """Converte uma string formatada como moeda (R$) de volta para float."""
    if value_str is None: return 0.0
    try:
        cleaned_str = str(value_str).replace('R$', '').strip().replace('.', '').replace(',', '.')
        return float(cleaned_str)
    except (ValueError, TypeError):
        return 0.0

def set_window_icon(window, icon_name="Invento+.ico"):
    """Tenta definir o ícone da janela."""
    try:
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            # Assume que utils.py está no mesmo diretório que main.py
            base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        icon_path = os.path.join(base_path, icon_name)
        res_icon_path = os.path.join(base_path, 'resources', icon_name)

        if os.path.exists(icon_path):
            window.iconbitmap(default=icon_path) # Usar default= pode ser mais robusto
        elif os.path.exists(res_icon_path):
             window.iconbitmap(default=res_icon_path)
        else:
             print(f"Aviso: Ícone '{icon_name}' não encontrado em '{base_path}' ou subdiretório 'resources'.")
    except tk.TclError as e:
        print(f"Aviso: Não foi possível definir o ícone '{icon_name}'. Erro Tcl: {e}")
    except Exception as e:
        print(f"Erro inesperado ao definir o ícone '{icon_name}': {e}")

def center_toplevel(toplevel, parent):
    """Centraliza uma janela Toplevel em relação à janela pai."""
    toplevel.update_idletasks()
    parent_x = parent.winfo_x(); parent_y = parent.winfo_y()
    parent_w = parent.winfo_width(); parent_h = parent.winfo_height()
    win_w = toplevel.winfo_width(); win_h = toplevel.winfo_height()
    x = parent_x + (parent_w - win_w) // 2
    y = parent_y + (parent_h - win_h) // 2
    screen_w = parent.winfo_screenwidth(); screen_h = parent.winfo_screenheight()
    x = max(0, min(x, screen_w - win_w)); y = max(0, min(y, screen_h - win_h))
    toplevel.geometry(f"+{x}+{y}")
    toplevel.lift()

def get_ordem_atual(ordem_dict):
    """Obtém a última coluna e direção de ordenação de um dicionário."""
    if ordem_dict and isinstance(ordem_dict, dict):
        try:
            last_col = list(ordem_dict.keys())[-1]
            return last_col, ordem_dict[last_col]
        except IndexError:
            return None, None
    return None, None

# --- NOVA FUNÇÃO MOVIDA PARA CÁ ---
def check_dependencies(parent_window=None):
    """Verifica dependências opcionais e exibe aviso se faltarem."""
    missing = []
    if not REPORTLAB_AVAILABLE:
        missing.append("ReportLab (pip install reportlab) - Necessário para gerar PDF/Contrato/Saída.")
    if not OPENPYXL_AVAILABLE:
        missing.append("Openpyxl (pip install openpyxl) - Necessário para exportar para Excel formatado.")
    # Adicione outras verificações aqui se necessário

    if missing:
        message = "Bibliotecas opcionais não encontradas:\n\n" + "\n".join(missing) + "\n\nFuncionalidades relacionadas estarão desabilitadas."
        # Usa a janela pai fornecida para o messagebox, se houver
        messagebox.showwarning("Dependências Opcionais Ausentes", message, parent=parent_window)

# Chama a configuração de locale quando o módulo é importado
setup_locale()
