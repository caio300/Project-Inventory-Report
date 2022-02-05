import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(self, file_name):
        if "csv" in file_name:
            with open(file_name) as file:
                data = csv.DictReader(file)
                new_data = [row for row in data]
                return new_data
        else:
            raise ValueError("Erro! Arquivo inválido")
