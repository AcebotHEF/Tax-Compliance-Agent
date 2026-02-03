from langchain_core.prompts import PromptTemplate

tax_template = PromptTemplate.from_template("""
You are a tax compliance auditor AI.

Here is a company’s financial summary:

{tax_table}

Please:
1. Identify any discrepancies in VAT reporting (collected vs paid).
2. Estimate whether income tax paid is reasonable based on net profit.
3. Flag any areas of non-compliance or audit risk.
4. Recommend corrective actions.

Be concise and audit-ready in tone.
""")