import read_data
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt


# retorna o diretório de trabalho atual de um processo + a pasta onde está os dados dos elétros
directory =  '/Users/brunamartini/code/power_signature' + '/ACS-F1'

read_data.signature(directory)

