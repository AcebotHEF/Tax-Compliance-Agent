import pandas as pd

def get_tax_records():
    data = {
        "Category": ["Revenue", "COGS", "Operating Expenses", "VAT Collected", "VAT Paid", "Payroll Tax", "Corporate Income Tax Paid"],
        "Amount": [120000, 40000, 25000, 8000, 3500, 7000, 5000]
    }
    return pd.DataFrame(data)