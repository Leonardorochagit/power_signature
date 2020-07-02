import read_data
import xml.etree.ElementTree as ET
import os


# retorna o diretório de trabalho atual de um processo + a pasta onde está os dados dos elétros
directory = os.getcwd() + '/ACS-F1'

read_data.signature(directory)

