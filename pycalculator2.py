import tkinter as tk
import sqlite3

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'),
                                    textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root, width=400, height=272.5, bg="grey")
        self.buttons_frame.pack()

        # Layout for buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'History']
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '=':
                    btn = tk.Button(self.buttons_frame, text=btn_text, fg="black", width=10, height=3,
                                    bd=0, bg="#ffa07a", cursor="hand2", command=self.evaluate)
                elif btn_text == 'C':
                    btn = tk.Button(self.buttons_frame, text=btn_text, fg="black", width=32, height=3,
                                    bd=0, bg="#f08080", cursor="hand2", command=self.clear)
                    btn.grid(row=i, column=j, columnspan=3)
                    continue
                elif btn_text == 'History':
                    btn = tk.Button(self.buttons_frame, text=btn_text, fg="black", width=10, height=3,
                                    bd=0, bg="#add8e6", cursor="hand2", command=self.show_history)
                    btn.grid(row=i, column=j + 3)
                    continue
                else:
                    btn = tk.Button(self.buttons_frame, text=btn_text, fg="black", width=10, height=3,
                                    bd=0, bg="#fff", cursor="hand2", command=lambda txt=btn_text: self.click(txt))

                btn.grid(row=i, column=j)

        # Initialize DB
        self.conn = sqlite3.connect("pycalc.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS calc_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input1 TEXT,
                input2 TEXT,
                symbol TEXT,
                output TEXT
            )
        """)
        self.conn.commit()

    def click(self, item):
        self.input_text.set(self.input_text.get() + str(item))

    def clear(self):
        self.input_text.set("")

    def evaluate(self):
        expression = self.input_field.get()
        try:
            result = eval(expression)
            self.input_text.set(str(result))

            # Store in DB: full expression as input1, output as result
            self.cursor.execute("""
                INSERT INTO calc_data (input1, input2, symbol, output)
                VALUES (?, ?, ?, ?)
            """, (expression, "", "", str(result)))
            self.conn.commit()

        except Exception as e:
            self.input_text.set("Error")

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x300")

        history_text = tk.Text(history_window, wrap=tk.WORD)
        history_text.pack(expand=True, fill=tk.BOTH)

        self.cursor.execute("SELECT input1, output FROM calc_data")
        rows = self.cursor.fetchall()
        for row in rows:
            input1, output = row
            history_text.insert(tk.END, f"{input1} = {output}\n")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
