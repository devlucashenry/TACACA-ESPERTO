import tkinter as tk
from tela_produtos import tela_produtos

pedido_atual = {}

def tela_novo_pedido(tela_anterior):
    if tela_anterior:
        tela_anterior.destroy()

    root = tk.Tk()
    root.title("Novo Pedido")
    root.geometry("400x300")

    pedido_atual["id_pedido"] = 1
    pedido_atual["itens"] = []

    tk.Label(
        root,
        text=f"Pedido Nº {pedido_atual['id_pedido']}",
        font=("Arial", 16)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Adicionar Produtos",
        width=25,
        height=2,
        command=lambda: tela_produtos(root, pedido_atual)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Fechar",
        width=25,
        command=root.destroy
    ).pack(pady=10)

    root.mainloop()
