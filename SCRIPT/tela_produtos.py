import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def tela_produtos(tela_anterior, pedido):
    tela_anterior.destroy()

    root = tk.Tk()
    root.title("Produtos")
    root.geometry("400x400")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT ID_PRODUTO, DESCRICAO, TIPO, PRECO
        FROM PRODUTO
        WHERE ATIVO = 'S'
        ORDER BY DESCRICAO
    """)

    produtos = cur.fetchall()

    tk.Label(
        root,
        text="Selecione os produtos",
        font=("Arial", 16)
    ).pack(pady=10)

    lista = tk.Listbox(root, width=40, height=10)
    lista.pack(pady=10)

    # agora bate exatamente com a query
    for id_prod, descricao, tipo, preco in produtos:
        lista.insert(
            tk.END,
            f"{descricao} ({tipo}) - R$ {preco:.2f}"
        )

    def adicionar():
        if not lista.curselection():
            messagebox.showwarning("Atenção", "Selecione um produto")
            return

        index = lista.curselection()[0]
        id_prod, descricao, tipo, preco = produtos[index]

        pedido["itens"].append({
            "id_produto": id_prod,
            "descricao": descricao,
            "tipo": tipo,
            "preco": float(preco)
        })

        messagebox.showinfo(
            "Adicionado",
            f"{descricao} adicionado ao pedido"
        )

    tk.Button(
        root,
        text="Adicionar ao Pedido",
        width=25,
        command=adicionar
    ).pack(pady=10)

    def voltar():
        cur.close()
        conn.close()
        root.destroy()

    tk.Button(
        root,
        text="Voltar",
        width=25,
        command=voltar
    ).pack(pady=10)

    root.mainloop()
