import sys
from cx_Freeze import setup, Executable
import os

# --- Informações da Aplicação ---
APP_NAME = "EletroTec"
APP_VERSION = "1.6" # Mantenha sincronizado com utils.py se desejar
APP_DESCRIPTION = "Sistema de Controle de Estoque e Orçamento"
MAIN_SCRIPT = "main.py"
ICON_FILE = "Invento+.ico" # Nome do arquivo de ícone

# --- Determinar a Base (GUI ou Console) ---
# Base=None cria um app de console (útil para debug)
# Base="Win32GUI" cria um app GUI sem console no Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# --- Opções de Build ---
# Adicione aqui pacotes que o cx_Freeze pode ter dificuldade em encontrar automaticamente.
# Verifique os imports em todos os seus arquivos .py.
packages = [
    "tkinter",
    "sqlite3",
    "datetime",
    "hashlib",
    "locale",
    "traceback",
    "os",
    "sys",
    "reportlab", # Necessário se REPORTLAB_AVAILABLE = True
    "reportlab.platypus",
    "reportlab.lib.styles",
    "reportlab.lib.units",
    "reportlab.lib.enums",
    "reportlab.lib.colors",
    "reportlab.lib.pagesizes",
    "openpyxl", # Necessário se OPENPYXL_AVAILABLE = True
    "openpyxl.styles",
    # "pandas", # Inclua se for usar Pandas no futuro
]

# Módulos que talvez precisem ser incluídos explicitamente (geralmente não necessário para estes)
includes = []

# Módulos que você tem certeza que não são necessários (podem reduzir o tamanho)
excludes = [
    "unittest",
    "test",
    "pydoc",
    "pydoc_data",
    "distutils",
    "xmlrpc",
    "email",
    # Adicione outros se souber que não são usados
]

# Arquivos adicionais para incluir no build (ícones, bases de dados iniciais, etc.)
# Formato: lista de tuplas ('caminho/origem', 'caminho/destino_no_build')
# O destino é relativo ao diretório do executável.
include_files = [
    (ICON_FILE, ICON_FILE), # Copia o ícone para a raiz do build
    # Se o ícone estiver em 'resources': ('resources/Invento+.ico', 'resources/Invento+.ico')
    # NÃO inclua os arquivos .db se você quer que a aplicação os crie
    # Se quisesse incluir um DB inicial: ('estoque_orcamento.db', 'estoque_orcamento.db')
]

# Configuração específica do build_exe
build_exe_options = {
    "packages": packages,
    "includes": includes,
    "excludes": excludes,
    "include_files": include_files,
    "optimize": 2, # Otimização do bytecode
    # "zip_include_packages": ["*"], # Força tudo para dentro do zip (pode afetar startup)
    # "zip_exclude_packages": [],
}

# --- Configuração do Executável ---
executables = [
    Executable(
        MAIN_SCRIPT,
        base=base,
        target_name=f"{APP_NAME}.exe" if sys.platform == "win32" else APP_NAME, # Nome do executável final
        icon=ICON_FILE # Define o ícone do executável
    )
]

# --- Executar o Setup ---
setup(
    name="EletroTec",
    version=1.6,
    description=APP_DESCRIPTION,
    options={"build_exe": build_exe_options},
    executables=executables,
)

print("\n--- Build Concluído ---")
print(f"Executável gerado em: build/exe.{sys.platform}-{'.'.join(map(str, sys.version_info[:2]))}")
print("-----------------------\n")