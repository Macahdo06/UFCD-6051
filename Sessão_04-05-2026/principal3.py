import tkinter as tk
from PIL import Image, ImageTk  # precisa de instalar: pip install pillow

# Criar janela
janela = tk.Tk()
janela.title("Ficha do Aluno - Instalações Elétricas")
janela.geometry("400x500")

# ===== FOTO DO ALUNO =====
# Substitui "foto.jpg" pelo caminho da tua imagem
imagem = Image.open(r"C:\Users\macha\OneDrive\Ambiente de Trabalho\Faisca\UFCD6051 - Programação\Sessão_04-05-2026\peaky..jpg")
imagem = imagem.resize((150, 150))
foto = ImageTk.PhotoImage(imagem)

label_foto = tk.Label(janela, image=foto)
label_foto.pack(pady=10)

# ===== NOME DO ALUNO =====
label_nome = tk.Label(janela, text="Nome: Rui Machado", font=("Arial", 14))
label_nome.pack()

# ===== UFCDs =====
label_titulo = tk.Label(janela, text="UFCDs - Instalações Elétricas", font=("Arial", 12, "bold"))
label_titulo.pack(pady=10)

ufcds = [
    "UFCD 1 - Segurança em instalações elétricas",
    "UFCD 2 - Eletricidade básica",
    "UFCD 3 - Instalações elétricas residenciais",
    "UFCD 4 - Máquinas elétricas"
]

for ufcd in ufcds:
    label = tk.Label(janela, text=ufcd)
    label.pack(anchor="w", padx=20)

# Executar janela
janela.mainloop()

