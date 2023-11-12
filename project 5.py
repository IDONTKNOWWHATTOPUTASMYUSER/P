import tkinter as tk
from tkinter import ttk

class FinancialCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Calculator bb<333")

        # Variables (end meeeeeee)
        self.principal_var = tk.DoubleVar()
        self.interest_rate_var = tk.DoubleVar()
        self.investment_time_var = tk.DoubleVar()
        self.loan_amount_var = tk.DoubleVar()
        self.loan_interest_rate_var = tk.DoubleVar()
        self.loan_duration_var = tk.DoubleVar()

        # widgets(tf r theseeeeee)
        self.create_widgets()

    def calculate_compound_interest(self):
        principal = self.principal_var.get()
        rate = self.interest_rate_var.get()
        time = self.investment_time_var.get()

        result = self.compound_interest(principal, rate, time)
        self.result_label.config(text=f"The future value of the investment is: ${result:.2f}")

    def calculate_loan_payment(self):
        loan_amount = self.loan_amount_var.get()
        rate = self.loan_interest_rate_var.get()
        time = self.loan_duration_var.get()

        result = self.loan_payment(loan_amount, rate, time)
        self.result_label.config(text=f"The monthly payment for the loan is: ${result:.2f}")

    def create_widgets(self):
        # Investment (I wanna dieeeeee)
        investment_frame = ttk.LabelFrame(self.root, text="Investment Calculator")
        investment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(investment_frame, text="Principal Amount: $").grid(row=0, column=0, sticky="w")
        ttk.Entry(investment_frame, textvariable=self.principal_var).grid(row=0, column=1)

        ttk.Label(investment_frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="w")
        ttk.Entry(investment_frame, textvariable=self.interest_rate_var).grid(row=1, column=1)

        ttk.Label(investment_frame, text="Investment Time (years):").grid(row=2, column=0, sticky="w")
        ttk.Entry(investment_frame, textvariable=self.investment_time_var).grid(row=2, column=1)

        ttk.Button(investment_frame, text="Calculate", command=self.calculate_compound_interest).grid(row=3, column=0, columnspan=2)

        # Loan Frame (I AM IN MISERYYYYYYYYY)
        loan_frame = ttk.LabelFrame(self.root, text="Loan Calculator")
        loan_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(loan_frame, text="Loan Amount: $").grid(row=0, column=0, sticky="w")
        ttk.Entry(loan_frame, textvariable=self.loan_amount_var).grid(row=0, column=1)

        ttk.Label(loan_frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="w")
        ttk.Entry(loan_frame, textvariable=self.loan_interest_rate_var).grid(row=1, column=1)

        ttk.Label(loan_frame, text="Loan Duration (years):").grid(row=2, column=0, sticky="w")
        ttk.Entry(loan_frame, textvariable=self.loan_duration_var).grid(row=2, column=1)

        ttk.Button(loan_frame, text="Calculate", command=self.calculate_loan_payment).grid(row=3, column=0, columnspan=2)

        # Label
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

    @staticmethod
    def compound_interest(principal, rate, time):
        n = 12  
        rate /= 100 
        return principal * (1 + rate / n) ** (n * time)

    @staticmethod
    def loan_payment(principal, rate, time):
        n = 12 * time 
        monthly_rate = rate / 12 / 100 
        return principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialCalculatorGUI(root)
    root.mainloop()


# tq random dude from youtube i love u
