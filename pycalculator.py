import tkinter as tk
import mysql.connector as mysql

class Calculator:
    def __init__(self):
        # Database connection
        self.db = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="pycalc"
        )
        self.cursor = self.db.cursor()

        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("900x650")

        # Output field
        self.output_field = tk.Label(self.window, width=36, borderwidth=5, relief="groove", height=2, font=("Arial", 16))
        self.output_field.grid(row=0, column=0, columnspan=4)

        # Input field
        self.input_field = tk.Entry(self.window, width=36, borderwidth=5, relief="groove", font=("Arial", 16))
        self.input_field.grid(row=1, column=0, columnspan=4)

        # Buttons
        buttons = [
            '(', ')', 'C', 'CE',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 2
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, font=("Arial", 21),
                      command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Show History button
        tk.Button(self.window, text="Show History", font=("Arial", 14), width=20,
                  command=self.show_history).grid(row=row_val, column=0, columnspan=4, pady=10)

    def click_button(self, button):
        if button == '=' and self.input_field.get():
            try:
                expression = self.input_field.get()
                result = eval(expression)
                self.output_field.config(text=str(result))

                # Extract operands and operator
                tokens = self.tokenize_expression(expression)
                if len(tokens) == 3 and all(tokens):
                    input1, symbol, input2 = tokens
                    self.cursor.execute(
                        "INSERT INTO calc_data (input1, input2, symbol, output) VALUES (%s, %s, %s, %s)",
                        (input1, input2, symbol, str(result))
                    )
                    self.db.commit()
            except Exception:
                self.output_field.config(text="Error")
        elif button == 'C':
            self.input_field.delete(0, tk.END)
            self.output_field.config(text="")
        elif button == 'CE':
            current_text = self.input_field.get()
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, current_text[:-1])
        else:
            self.input_field.insert(tk.END, button)

    def tokenize_expression(self, expression):
        for symbol in ['+', '-', '*', '/']:
            if symbol in expression:
                parts = expression.split(symbol)
                if len(parts) == 2:
                    return [parts[0].strip(), symbol, parts[1].strip()]
                if len(parts) == 3:
                    return [parts[0].strip(), symbol, parts[1].strip() + parts[2].strip()]
        return ["", "", ""]

    def show_history(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Calculation History")
        history_window.geometry("500x400")

        history_text = tk.Text(history_window, wrap=tk.WORD)
        history_text.pack(expand=True, fill=tk.BOTH)

        self.cursor.execute("SELECT input1, symbol, input2, output FROM calc_data")
        rows = self.cursor.fetchall()
        for row in rows:
            input1, symbol, input2, output = row
            history_text.insert(tk.END, f"{input1} {symbol} {input2} = {output}\n")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()


# # This is a simple calculator application using Tkinter and MySQL database
# # It allows users to perform basic arithmetic operations and stores the history of calculations in a database
# # The application has a GUI with buttons for numbers, operators, and a history feature
# # The code is well-structured and follows good programming practices
