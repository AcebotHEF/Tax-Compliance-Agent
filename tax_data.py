import pandas as pd

def get_tax_records():
    """
    Returns a comprehensive dataframe of tax and financial records,
    including potential compliance red flags for the AI to detect.
    """
    data = {
        "Category": [
            "Total Revenue (Gross)", 
            "Cost of Goods Sold (COGS)", 
            "Gross Profit",
            "Operating Expenses (Rent/Utilities)", 
            "Staff Salaries & Wages",
            "Marketing & Advertising",
            "Professional Services (Legal/Audit)",
            "Uncategorized Cash Withdrawals",  # RISK FLAG
            "VAT Collected (Output Tax)", 
            "VAT Paid on Purchases (Input Tax)", 
            "Net VAT Payable",
            "PAYE Remitted (Payroll Tax)", 
            "Pension Contributions (Employer)",
            "Corporate Income Tax Paid",
            "Regulatory Penalties (Late Filing)" # RISK FLAG
        ],
        "Amount": [
            500000.00, 
            210000.00, 
            290000.00,
            45000.00, 
            120000.00,
            15000.00,
            8500.00,
            12500.00,  # Suspicious high cash withdrawal
            37500.00, 
            14200.00, 
            23300.00,
            18000.00,
            9500.00,
            15000.00,  # Seemingly low tax for the revenue
            2500.00    # Penalty indicates compliance issues
        ]
    }
    return pd.DataFrame(data)