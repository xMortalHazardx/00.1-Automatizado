import tkinter as tk
import json

with open("/home/machine/Documents/Automatizado/00.1-Automatizado/chamado.json", "r") as file:
    chamado = json.load(file)

print(chamado)

def mostrar_texto():
    texto = entry.get()  # Obtém o texto inserido no Entry
    label_resultado.config(text=f"Você digitou: {texto}")
def on_focus_in(event):
    if entry.get() == "Digite seu nome aqui...":  # Se o texto for o texto de dica
        entry.delete(0, tk.END)  # Limpa o texto de dica

def on_focus_out(event):
    if entry.get() == "":  # Se o usuário deixou o campo vazio
        entry.insert(0, "Digite seu nome aqui...")  # Coloca o texto de dica novamente

# Criando a janela principal
root = tk.Tk()
root.title("Chamado Passivo")
root.minsize(400,300)

# Criando o Entry (textbox de uma linha)

entry = tk.Entry(root,width=30)

entry.insert(0, "Digite o usuário aqui...")  # Texto sugestivo inicial
entry.bind("<FocusIn>", on_focus_in)  # Quando o campo recebe foco
entry.bind("<FocusOut>", on_focus_out)  # Quando o campo perde o foco
entry.pack(pady=10)

# Criando um botão para mostrar o texto
botao = tk.Button(root, text="Mostrar Texto", command=mostrar_texto)
botao.pack(pady=5)

# Criando um rótulo (label) para mostrar o texto inserido
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Iniciando o loop da interface gráfica
root.mainloop()
