import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def import_data(file_name, relatory_type):
        if "csv" in file_name:
            data = read_csv(file_name)

        return relatory(relatory_type, data)


def relatory(relatory_type, data):
    if relatory_type == "simples":
        return SimpleReport.generate(data)
    if relatory_type == "completo":
        return CompleteReport.generate(data)


def read_csv(file_name):
    with open(file_name) as file:
        data = csv.DictReader(file)
        new_data = [row for row in data]
        return new_data
