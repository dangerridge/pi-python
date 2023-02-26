import tkinter as tk
import decimal
import tkinter.ttk as ttk

def pi_spigot(n):
    decimal.getcontext().prec = n + 100
    pi = decimal.Decimal(0)
    for k in range(n):
        pi += decimal.Decimal(1) / decimal.Decimal(16 ** k) * (decimal.Decimal(4) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(1)) - decimal.Decimal(2) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(4)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(5)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(6)))
    return str(pi)[:n+2]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter the number of digits of pi to calculate:")
        self.label.pack(side="top")

        self.entry = tk.Entry(self)
        self.entry.pack(side="top")

        self.button = tk.Button(self, text="Calculate", command=self.calculate_pi)
        self.button.pack(side="top")

        self.result_text = tk.Text(self, wrap="word")
        self.result_text.pack(side="top", fill="both", expand=True)

        self.copy_button = ttk.Button(self, text="Copy", command=self.copy_result)
        self.copy_button.pack(side="top")

        self.result_scrollbar = ttk.Scrollbar(self.result_text)
        self.result_scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=self.result_scrollbar.set)
        self.result_scrollbar.config(command=self.result_text.yview)

    def calculate_pi(self):
        n = int(self.entry.get())
        pi = pi_spigot(n)
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", f"Pi with {n} digits of accuracy:\n{pi}")
        self.result_text.config(state="disabled")

    def copy_result(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.result_text.get("1.0", "end"))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
