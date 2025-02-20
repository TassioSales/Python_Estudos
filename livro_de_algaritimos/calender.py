import calendar
import tkinter as tk
from tkinter import ttk, simpledialog

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal temporariamente

    # Perguntar ao usuário o ano
    year = simpledialog.askinteger("Input", "Enter the year:", minvalue=1, maxvalue=9999)

    # Perguntar ao usuário o mês, permitindo valor vazio
    month = simpledialog.askstring("Input", "Enter the month (1-12) or leave empty for full year:")

    root.deiconify()  # Mostrar a janela principal
    root.title("Calendário")

    # Ajustar o tamanho da janela com base na entrada do usuário
    if month and month.isdigit() and 1 <= int(month) <= 12:
        root.geometry("400x400")  # Tamanho menor para um mês específico
    else:
        root.geometry("1000x600")  # Tamanho maior para o ano completo

    root.resizable(False, False)

    # Criar um frame para organizar os elementos e adicionar rolagem
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    # Criar um canvas para permitir rolagem
    canvas = tk.Canvas(frame)
    scrollbar_y = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    # Configurar o canvas para funcionar com o frame de rolagem
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adicionar as barras de rolagem ao canvas
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    # Exibir o canvas e as barras de rolagem
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Criar um widget de texto somente leitura
    text = tk.Text(scrollable_frame, wrap=tk.NONE, font=("Courier", 12), bg="white", width=100, height=20)
    text.pack(fill=tk.BOTH, expand=True)  # Expande para preencher o espaço disponível

    # Obter o calendário com base na escolha do usuário
    cal = calendar.TextCalendar(calendar.SUNDAY)

    if month and month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            title = f"{calendar.month_name[month]} {year}"
            cal_text = cal.formatmonth(year, month)
        else:
            title = f"Year {year}"
            cal_text = cal.formatyear(year)
    else:
        title = f"Year {year}"
        cal_text = cal.formatyear(year)

    # Exibir título e calendário
    month_year_label = ttk.Label(scrollable_frame, text=title, font=("Arial", 14, "bold"))
    month_year_label.pack()

    text.insert(tk.END, cal_text)
    text.config(state=tk.DISABLED)

    # Configurar o canvas para rolar corretamente
    canvas.update_idletasks()  # Atualiza o canvas após inserir texto

    root.mainloop()

if __name__ == '__main__':
    main()
