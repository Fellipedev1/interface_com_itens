import tkinter as tk
from tkinter import ttk

def adicionar_item():
    nome = nome_entry.get()
    descricao = descricao_entry.get()
    preco = preco_entry.get()
    quantidade = quantidade_entry.get()

    if nome and descricao and preco and quantidade:
        item = {
            "Nome": nome,
            "Descrição": descricao,
            "Preço": preco,
            "Quantidade": quantidade
        }

def remover_item():
    nome = nome_remover_entry.get()
    for item in itens:
        if item["Nome"] == nome:
            itens.remove(item)
            status_label_remover["text"] = "Item removido com sucesso!"
            nome_remover_entry.delete(0, tk.END)
            return
    status_label_remover["text"] = "O item não está na lista."

def pesquisar_item():
    nome = nome_pesquisar_entry.get()
    for item in itens:
        if item["Nome"] == nome:
            status_label_pesquisar["text"] = f"Item encontrado:\nNome: {item['Nome']}\nDescrição: {item['Descrição']}\nPreço: {item['Preço']}\nQuantidade: {item['Quantidade']}"
            nome_pesquisar_entry.delete(0, tk.END)
            return
    status_label_pesquisar["text"] = "O item não está na lista."

def criar_interface():
    root = tk.Tk()
    root.title("😎😎😎😎 Supermercado do felipão 😎😎😎😎 ")

    # Definir cor de fundo da janela principal
    root.configure(background="Teal")

    # este trecho de codigo cria as abas do programa
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10)

    adicionar_tab = ttk.Frame(notebook)
    notebook.add(adicionar_tab, text="Adicionar Item 👨‍💻 ")

    remover_tab = ttk.Frame(notebook)
    notebook.add(remover_tab, text="Remover Item 👨‍💻 ")

    pesquisar_tab = ttk.Frame(notebook)
    notebook.add(pesquisar_tab, text="Pesquisar Item 👨‍💻 ")

    # aba "Adicionar Item"
    adicionar_frame = tk.Frame(adicionar_tab)
    adicionar_frame.pack(pady=10)

    nome_label = tk.Label(adicionar_frame, text="Nome:")
    nome_label.grid(row=0, column=0, sticky="e")

    nome_entry = tk.Entry(adicionar_frame)
    nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    descricao_label = tk.Label(adicionar_frame, text="Descrição:")
    descricao_label.grid(row=1, column=0, sticky="e")

    descricao_entry = tk.Entry(adicionar_frame)
    descricao_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    preco_label = tk.Label(adicionar_frame, text="Preço:")
    preco_label.grid(row=2, column=0, sticky="e")

    preco_entry = tk.Entry(adicionar_frame)
    preco_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    quantidade_label = tk.Label(adicionar_frame, text="Quantidade:")
    quantidade_label.grid(row=3, column=0, sticky="e")

    quantidade_entry = tk.Entry(adicionar_frame)
    quantidade_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    adicionar_button = tk.Button(adicionar_frame, text="Adicionar", command=adicionar_item)
    adicionar_button.grid(row=4, column=0, columnspan=2, pady=10)

    # esta aba adciona um item 
    remover_frame = tk.Frame(remover_tab)
    remover_frame.pack(pady=10)

    nome_remover_label = tk.Label(remover_frame, text="Nome do item a ser removido:")
    nome_remover_label.grid(row=0, column=0, sticky="e")

    nome_remover_entry = tk.Entry(remover_frame)
    nome_remover_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    remover_button = tk.Button(remover_frame, text="Remover", command=remover_item)
    remover_button.grid(row=1, column=0, columnspan=2, pady=10)

    status_label_remover = tk.Label(remover_tab, text="")
    status_label_remover.pack(pady=10)

    # essse trecho de codigo pesquisa um item
    pesquisar_frame = tk.Frame(pesquisar_tab)
    pesquisar_frame.pack(pady=10)

    nome_pesquisar_label = tk.Label(pesquisar_frame, text="Nome do item a ser pesquisado:")
    nome_pesquisar_label.grid(row=0, column=0, sticky="e")

    nome_pesquisar_entry = tk.Entry(pesquisar_frame)
    nome_pesquisar_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    pesquisar_button = tk.Button(pesquisar_frame, text="Pesquisar", command=pesquisar_item)
    pesquisar_button.grid(row=1, column=0, columnspan=2, pady=10)

    status_label_pesquisar = tk.Label(pesquisar_tab, text="")
    status_label_pesquisar.pack(pady=10)

    # esse trecho coloca um botao
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    sair_button = tk.Button(button_frame, text="Sair", command=root.quit)
    sair_button.grid(row=0, column=0)

    # Centralize a janela na tela
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()

itens = []
criar_interface()
