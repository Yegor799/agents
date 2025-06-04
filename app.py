# app.py
import streamlit as st
import asyncio
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def macro_agent(news):
    response = await client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты макроэкономический аналитик. Делай выводы по новостям."},
            {"role": "user", "content": news}
        ]
    )
    return response.choices[0].message.content

async def quant_agent(stock_data):
    response = await client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты количественный аналитик. Проанализируй технические индикаторы."},
            {"role": "user", "content": stock_data}
        ]
    )
    return response.choices[0].message.content

async def fundamental_agent(company_name):
    response = await client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты фундаментальный аналитик. Оцени финансовые показатели компании."},
            {"role": "user", "content": f"Анализируй компанию {company_name}"}
        ]
    )
    return response.choices[0].message.content

async def portfolio_manager(news, stock_data, company_name):
    macro_task = asyncio.create_task(macro_agent(news))
    quant_task = asyncio.create_task(quant_agent(stock_data))
    fundamental_task = asyncio.create_task(fundamental_agent(company_name))

    macro_result, quant_result, fundamental_result = await asyncio.gather(
        macro_task, quant_task, fundamental_task
    )

    summary_prompt = f"""
    Макро: {macro_result}
    Квант: {quant_result}
    Фундамент: {fundamental_result}

    На основе этих данных, стоит ли покупать акции компании {company_name}?
    """

    final_response = await client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты главный инвестиционный аналитик. Суммируй данные и прими решение."},
            {"role": "user", "content": summary_prompt}
        ]
    )

    return macro_result, quant_result, fundamental_result, final_response.choices[0].message.content

# Интерфейс Streamlit
st.set_page_config(page_title="AI Portfolio Manager", layout="wide")
st.title("🤖 Многослойный AI-анализ инвестиций")

with st.form("input_form"):
    news = st.text_area("📰 Макроэкономические новости", height=150)
    stock_data = st.text_area("📈 Данные технического анализа", height=150)
    company_name = st.text_input("🏢 Название компании")
    submitted = st.form_submit_button("Анализировать")

if submitted:
    with st.spinner("Агенты анализируют..."):
        macro, quant, fundamental, decision = asyncio.run(portfolio_manager(news, stock_data, company_name))

    st.subheader("🌍 Макроэкономический анализ")
    st.write(macro)

    st.subheader("📊 Технический анализ")
    st.write(quant)

    st.subheader("📚 Фундаментальный анализ")
    st.write(fundamental)

    st.subheader("🧠 Финальное инвестиционное решение")
    st.success(decision)

