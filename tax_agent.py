from tax_data import get_tax_records
from tax_prompt import tax_template
from langchain.chat_models import ChatOpenAI

def analyze_tax():
    df = get_tax_records()
    table = df.to_string(index=False)

    llm = ChatOpenAI(temperature=0.2)
    prompt = tax_template.format(tax_table=table)
    result = llm.predict(prompt)
    return df, result