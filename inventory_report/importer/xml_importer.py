import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    def import_data(self, file_name):
        if "csv" in file_name:
            with open(file_name) as file:
                data = ET.parse(file)
                itemlist = data.getroot()

                complete_list = []
                for item in itemlist:
                    items = {}
                    for it in item:
                        items[it.tag] = it.text
                    complete_list.append(items)

                return complete_list
        else:
            raise ValueError("Erro! Arquivo inválido")
