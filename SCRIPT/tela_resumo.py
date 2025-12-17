import tkinter as tk
from tela_pagamento import tela_pagamento

def tela_resumo(tela_anterior, pedido):
    tela_anterior.destroy()

    root = tk.Tk()
    root.title("Resumo do Pedido")
    root.geometry("400x350")

    tk.Label(root, text="Resumo", font=("Arial", 16)).pack(pady=10)

    total = 0
    for item in pedido["itens"]:
        tk.Label(
            root,
            text=f"{item['descricao']} - R$ {item['valor']:.2f}"
        ).pack()
        total += item["valor"]

    tk.Label(
        root,
        text=f"TOTAL: R$ {total:.2f}",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Button(
        root,
        text="Finalizar Pedido",
        width=25,
        height=2,
        command=lambda: tela_pagamento(root, pedido, total)
    ).pack(pady=10)

    root.mainloop()
