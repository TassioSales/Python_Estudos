# Calculadora de Bhaskara com Interface Gráfica (Tkinter)
import tkinter as tk
from tkinter import messagebox
import math

def calcular_baskara():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            resultado.set("❗ O valor de 'a' não pode ser zero!")
            label_resultado.config(fg='#d32f2f')
            return
        delta = b**2 - 4*a*c
        res = f"Δ (Delta): {delta}\n"
        if delta < 0:
            res += "❗ As raízes não são reais (delta negativo)."
            label_resultado.config(fg='#d32f2f')
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            res += f"Raiz 1: {raiz1}\nRaiz 2: {raiz2}\n"
            if delta == 0:
                res += "As raízes são reais e iguais."
            else:
                res += "As raízes são reais e diferentes."
            label_resultado.config(fg='#222')
        resultado.set(res)
    except ValueError:
        resultado.set("❗ Digite valores numéricos válidos.")
        label_resultado.config(fg='#d32f2f')

def limpar_campos():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    resultado.set("")
    label_resultado.config(fg='#222')
    entry_a.focus()

# Configuração da janela
root = tk.Tk()
root.title("Calculadora de Bhaskara")
root.geometry("400x390")
root.configure(bg="#f3f6fa")
root.resizable(False, False)

# Estilo geral
FONT_TITULO = ("Segoe UI", 15, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_INPUT = ("Segoe UI", 12)
FONT_BTN = ("Segoe UI", 11, "bold")
FONT_RESULT = ("Segoe UI", 11)

frame = tk.Frame(root, padx=24, pady=18, bg="#f3f6fa")
frame.pack(expand=True, fill=tk.BOTH)

label_titulo = tk.Label(frame, text="Equação do 2º Grau: ax² + bx + c = 0", font=FONT_TITULO, bg="#f3f6fa", fg="#1a237e")
label_titulo.pack(pady=(0,16))

row1 = tk.Frame(frame, bg="#f3f6fa")
row1.pack(pady=(0,12))
for lbl, var in zip(["a:", "b:", "c:"], ["a", "b", "c"]):
    tk.Label(row1, text=lbl, font=FONT_LABEL, bg="#f3f6fa").pack(side=tk.LEFT, padx=(0,2))
    entry = tk.Entry(row1, width=6, font=FONT_INPUT, justify='center', bd=2, relief=tk.GROOVE)
    entry.pack(side=tk.LEFT, padx=(0,10))
    if var == "a":
        entry_a = entry
    elif var == "b":
        entry_b = entry
    else:
        entry_c = entry

btn_frame = tk.Frame(frame, bg="#f3f6fa")
btn_frame.pack(pady=(0,10))
btn_calcular = tk.Button(btn_frame, text="Calcular", command=calcular_baskara, bg="#2196f3", fg="white", font=FONT_BTN, width=10, relief=tk.RAISED, activebackground="#1565c0")
btn_calcular.pack(side=tk.LEFT, padx=6)
btn_limpar = tk.Button(btn_frame, text="Limpar", command=limpar_campos, bg="#bdbdbd", fg="#222", font=FONT_BTN, width=10, relief=tk.RAISED, activebackground="#757575")
btn_limpar.pack(side=tk.LEFT, padx=6)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado, font=FONT_RESULT, bg="#f3f6fa", fg="#222", justify='left', wraplength=340, anchor='w')
label_resultado.pack(pady=12, fill=tk.X)

# Rodapé
footer = tk.Label(root, text="Desenvolvido por Você · Fórmula de Bhaskara", font=("Segoe UI", 9), bg="#e3e9f0", fg="#888", pady=6)
footer.pack(side=tk.BOTTOM, fill=tk.X)

entry_a.focus()
root.mainloop()
