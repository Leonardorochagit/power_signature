import xml.etree.ElementTree as ET
import os
import numpy as np
import csv
import math

#  Ler arquivo CSV
#  Calcular variáveis para arvore de decisão

def gain_of_information(variable, row_count, ent_p):
  peso_1 = variable/row_count
  peso_2 = (row_count-variable)/row_count

  ent_f1 = -(math.log(1/variable))/math.log(variable)
  ent_f2 = -(math.log(1/(row_count-variable)))/math.log((row_count-variable))

  gain = ent_p - (peso_1*ent_f1 + peso_2*ent_f2)
  return gain
class question:
  def __init__(self, text, gain_of_information, position):
    self.text = text
    self.gain_of_information = gain_of_information
    self.position = position

# calcula o número de linhas de um arquivo CSV (subtrai um para retirar o cabeçalho)
row_count = sum(1 for line in open('db_elet.csv')) - 1
# Cálcula entropia total da arvore
ent_p = -(math.log(1/row_count))/math.log(row_count)

frequencia = 0
angulo = 0
pot_r = 0
pot = 0
tensao = 0
corrente = 0

with open('db_elet.csv', 'r') as file:
  reader = csv.reader(file)
  for linha in reader:
    # frequencia = 50
    if float(linha[2]) == 50:
      frequencia = frequencia + 1
    # Angulo > 200
    if float(linha[1]) > 200:
      angulo = angulo + 1
    # potencia reativa > 0
    if float(linha[3]) > 0:
      pot_r = pot_r + 1
    # potencia > 50
    if float(linha[4]) > 50:
      pot = pot + 1
    # tensão > 230
    if float(linha[5]) > 230:
      tensao = tensao + 1
    # corrente > 0.1
    if float(linha[6]) > 0.1:
      corrente = corrente + 1

# ganho de informação da frequencia
frequencia = print(gain_of_information(frequencia, row_count, ent_p))
angulo = print(gain_of_information(angulo, row_count, ent_p))
pot_r = print(gain_of_information(pot_r, row_count, ent_p))
tensao = print(gain_of_information(tensao, row_count, ent_p))
corrente = print(gain_of_information(corrente, row_count, ent_p))


