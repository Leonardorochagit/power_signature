import xml.etree.ElementTree as ET
import os
import numpy as np
import csv

# retorna o diretório de trabalho atual de um processo + a pasta onde está os dados dos elétros
directory =  '/Users/brunamartini/code/power_signature' + '/ACS-F2'

# gera os nomes dos arquivos em uma árvore de diretórios, percorrendo a árvore de cima para baixo ou de baixo para cima.
list_dir = [x[0] for x in os.walk(directory)]
list_dir = list_dir[1:]
list_name = []

# criar planilha e popular cabeçalho
c = csv.writer(open("db_elet.csv", "w"))
c.writerow(["Eletro", "phAngle_min", "phAngle_max", "Freq_min", "Freq_max", "ReactPower_min", "ReactPower_max", "Power_min", "Power_max", "Volts_min", "Volts_max", "Cur_min", "Cur_max"])

for dirnames in list_dir:
  list_filenames = [x[2] for x in os.walk(dirnames)][0]
  for filenames in list_filenames:
    # Se a extenção do aqruivo for .mat
    if filenames.endswith(".mat"):
      cnt = 0
      list_mat_phAngle = []
      list_mat_freq = []
      list_mat_power = []
      list_mat_reacPower = []
      list_mat_rmsCur = []
      list_mat_rmsVolt = []
      for line in open(dirnames + '/' + filenames):
        li=line.strip()
        if not li.startswith("#"):
          line_float = list(map(float, li.split(' ')))
          cnt += 1
          if cnt == 1:
            list_mat_phAngle = line_float
          elif cnt == 2:
            list_mat_freq = line_float
          elif cnt == 3:
            list_mat_reacPower = line_float
          elif cnt == 4:
            list_mat_power = line_float
          elif cnt == 5:
            list_mat_rmsVolt = line_float
          elif cnt == 6:
            list_mat_rmsCur = line_float
        if cnt != 6:
          print(filenames);

      # salva valores em arquivo csv
      c.writerow([filenames,np.min(list_mat_phAngle),np.max(list_mat_phAngle),np.min(list_mat_freq),np.max(list_mat_freq),np.min(list_mat_reacPower),np.max(list_mat_reacPower),np.min(list_mat_power),np.max(list_mat_power),np.min(list_mat_rmsVolt),np.max(list_mat_rmsVolt),np.min(list_mat_rmsCur),np.max(list_mat_rmsCur)])
