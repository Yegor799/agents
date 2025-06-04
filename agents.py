# agents.py
from openai import OpenAI

client = OpenAI()

def macro_agent(input_data):
    return client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты макроэкономический аналитик. Делай выводы по новостям."},
            {"role": "user", "content": input_data}
        ]
    ).choices[0].message.content

def quant_agent(stock_data):
    return client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты количественный аналитик. Проанализируй технические индикаторы."},
            {"role": "user", "content": stock_data}
        ]
    ).choices[0].message.content

def fundamental_agent(company_name):
    return client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты фундаментальный аналитик. Оцени финансовые показатели компании."},
            {"role": "user", "content": f"Анализируй компанию {company_name}"}
        ]
    ).choices[0].message.content
