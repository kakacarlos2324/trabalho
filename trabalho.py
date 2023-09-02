import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para criar a janela de exibição da mensagem
def exibir_mensagem():
    nome = nome_entry.get()
    mensagem = mensagem_entry.get()
    
    if nome and mensagem:
        nova_janela = tk.Toplevel(root)
        nova_janela.title("Mensagem Enviada")
        
        mensagem_label = ttk.Label(nova_janela, text=f"Nome: {nome}\nMensagem: {mensagem}", padding=20)
        mensagem_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Botão para fechar a janela de exibição
        fechar_button = ttk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        fechar_button.grid(row=1, column=0, pady=10)
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos!")

# Configuração da janela principal
root = tk.Tk()
root.title("Envio de Mensagem")

# Estilo do aplicativo
style = ttk.Style()
style.configure("TButton", padding=10)
style.configure("TLabel", padding=10)

# Rótulo e campo de entrada para o nome
nome_label = ttk.Label(root, text="Nome:")
nome_label.grid(row=0, column=0, sticky="w")
# Definindo o valor padrão como "Carlos"
nome_entry = ttk.Entry(root, text="Carlos")
nome_entry.grid(row=0, column=1, padx=10, pady=10)

# Rótulo e campo de entrada para a mensagem
mensagem_label = ttk.Label(root, text="Mensagem:")
mensagem_label.grid(row=1, column=0, sticky="w")
mensagem_entry = ttk.Entry(root)
mensagem_entry.grid(row=1, column=1, padx=10, pady=10)

# Botão para enviar a mensagem
enviar_button = ttk.Button(root, text="Enviar", command=exibir_mensagem)
enviar_button.grid(row=2, columnspan=2, pady=20)

root.mainloop()