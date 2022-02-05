import csv
import json
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def import_data(file_name, relatory_type):
        if "csv" in file_name:
            data = read_csv(file_name)
        if "json" in file_name:
            data = read_json(file_name)
        if "xml" in file_name:
            data = read_xml(file_name)
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


def read_json(file_name):
    with open(file_name) as file:
        data = json.load(file)
        new_data = [row for row in data]
        return new_data


def read_xml(file_path):
    with open(file_path) as file:
        data = ET.parse(file)
        itemlist = data.getroot()

        complete_list = []
        for item in itemlist:
            items = {}
            for it in item:
                items[it.tag] = it.text
            complete_list.append(items)

        return complete_list
