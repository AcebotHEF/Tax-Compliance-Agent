from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tax_data import get_tax_records
from tax_prompt import tax_template

# Load API keys from .env file
load_dotenv()

def analyze_tax():
    """
    Fetches tax records and generates a compliance audit using Gemini.
    """
    try:
        # 1. Get the data
        df = get_tax_records()
        
        # Convert to string for the AI to read
        table = df.to_string(index=False)

        # 2. Initialize Gemini 
        # temperature=0.2 is good for auditing (precise, less creative)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

        # 3. Create the Chain (Prompt | LLM)
        chain = tax_template | llm

        # 4. Run the Chain
        # We pass the dictionary matching {tax_table} in the prompt
        response = chain.invoke({"tax_table": table})

        # Return dataframe (for display) and AI analysis text
        return df, response.content

    except Exception as e:
        return None, f"Error generating tax analysis: {e}"