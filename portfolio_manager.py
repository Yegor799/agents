# portfolio_manager.py
from agents import macro_agent, quant_agent, fundamental_agent

def run_portfolio_analysis(news, stock_data, company_name):
    print("Анализ макроэкономики...")
    macro_result = macro_agent(news)
    
    print("Технический анализ...")
    quant_result = quant_agent(stock_data)

    print("Фундаментальный анализ...")
    fundamental_result = fundamental_agent(company_name)

    # Решение
    print("\n🧠 Решение портфельного менеджера:")
    summary_prompt = f"""
    Макро: {macro_result}
    Квант: {quant_result}
    Фундамент: {fundamental_result}

    На основе этих данных, стоит ли покупать акции компании {company_name}?
    """
    from openai import OpenAI
    client = OpenAI()
    final_decision = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты главный инвестиционный аналитик. Суммируй данные и прими решение."},
            {"role": "user", "content": summary_prompt}
        ]
    ).choices[0].message.content

    print(final_decision)
