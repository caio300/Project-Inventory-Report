from datetime import date


class SimpleReport:
    def generate(data):
        today = date.today()
        max_date = []
        min_date = []
        stock = []

        for product in data:
            max_date.append(product["data_de_fabricacao"])
            if product["data_de_validade"] > today.strftime("%Y-%m-%d"):
                min_date.append(product["data_de_validade"])
            stock.append(product["nome_da_empresa"])

        max_stock = max(stock)

        return (
          f"Data de fabricação mais antiga: {min(max_date)}\n"
          f"Data de validade mais próxima: {min(min_date)}\n"
          f"Empresa com maior quantidade de produtos estocados: {max_stock}\n"
        )
