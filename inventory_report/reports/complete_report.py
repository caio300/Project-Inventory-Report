from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        quantity_items = []
        for product in data:
            name_company = product["nome_da_empresa"]
            quantity_items.append(f"{name_company}")
        quantity_stock = dict(Counter(quantity_items))

        text = ""
        for key, value in quantity_stock.items():
            text += f"- {key}: {value}\n"

        return (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa: \n"
            f"{text}"
        )
