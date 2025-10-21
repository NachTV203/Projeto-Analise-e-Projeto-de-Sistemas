import tkinter as tk

# Importa a classe de Login
from login import LoginScreen

# Tenta habilitar DPI Awareness no Windows para melhor renderização
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    print("DPI Awareness ativado.")
except ImportError:
    print("ctypes não encontrado (não Windows?).")
except AttributeError:
    print("Função SetProcessDpiAwareness não encontrada (versão antiga do Windows?).")
except Exception as e:
    print(f"Erro ao ativar DPI Awareness: {e}")

if __name__ == "__main__":
    # Cria a janela raiz para o login
    login_root = tk.Tk()
    # Instancia e inicia a tela de login
    login_app = LoginScreen(login_root)
    # Inicia o loop principal do Tkinter para a tela de login
    login_root.mainloop()

    print("Aplicação encerrada.")
