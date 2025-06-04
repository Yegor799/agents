# main.py
from portfolio_manager import run_portfolio_analysis

news = "Цены на нефть растут, инфляция в США снижается, ФРС может понизить ставку."
stock_data = "Индикаторы RSI показывают перепроданность, трендовые линии указывают на рост."
company_name = "Tesla"

run_portfolio_analysis(news, stock_data, company_name)
