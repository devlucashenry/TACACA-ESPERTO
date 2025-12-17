import tkinter as tk
from tela_pedido import tela_novo_pedido

def main():
    root = tk.Tk()
    root.title("Caixa - Barraca")
    root.geometry("400x300")

    tk.Label(
        root,
        text="BARRACA TACACÁ",
        font=("Arial", 18, "bold")
    ).pack(pady=30)

    tk.Button(
        root,
        text="Novo Pedido",
        width=20,
        height=2,
        command=lambda: tela_novo_pedido(root)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Sair",
        width=20,
        command=root.destroy
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
