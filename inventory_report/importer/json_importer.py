import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(self, file_name):
        if "json" in file_name:
            with open(file_name) as file:
                data = json.load(file)
                new_data = [row for row in data]
                return new_data
        else:
            raise ValueError("Erro! Arquivo inválido")
