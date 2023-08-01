# OJOK EMMANUEL NSUBUGA
# 21/U/06816/PS
# 2100706816

import tkinter as tk
from datetime import datetime


def calculate_amount(amount, tax):
    total_amount = amount + (amount * tax)
    return total_amount


def generate_receipt():
    # Get the input values
    customer = customer_entry.get()
    amount = float(amount_entry.get())
    staff = staff_entry.get()
    tax = float(tax_entry.get())

    # Calculate the total payment
    total_amount = calculate_amount(amount, tax)

    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the receipt 
    receipt = f"Receipt\n\nDate: {current_date}\n\ncustomer: {customer}\nAmount Paid: UGX {amount}\nCounter Person: {staff}\nTax: {tax}%\nTotal Payment: UGX {total_amount}"

    # Print the receipt
    receipt_text.delete('1.0', tk.END)
    receipt_text.insert(tk.END, receipt)


# Create the main window
window = tk.Tk()
window.title("OJOK EMMANUEL NSUBUGA")
window.geometry("300x500")

# Create the input fields
# name of customer
customer_label = tk.Label(window, text="Customer Name:")
customer_label.pack()
customer_entry = tk.Entry(window)
customer_entry.pack()

# Name of staff receiving payment
staff_label = tk.Label(window, text="Staff Name:")
staff_label.pack()
staff_entry = tk.Entry(window)
staff_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()


tax_label = tk.Label(window, text="Tax (percentage):")
tax_label.pack()
tax_entry = tk.Entry(window)
tax_entry.pack()

# Create the print receipt button
generate_button = tk.Button(window, text="Generate Receipt", command=generate_receipt)
generate_button.pack()

# Create the receipt area
receipt_text = tk.Text(window, height=10, width=50)
receipt_text.pack()

# to run the application
window.mainloop()
