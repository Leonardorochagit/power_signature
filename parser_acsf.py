import xml.etree.ElementTree as ET
import os

# retorna o diretório de trabalho atual de um processo + a pasta onde está os dados dos elétros
directory = '/Users/brunamartini/code/power_signature' + '/ACS-F1'
# gera os nomes dos arquivos em uma árvore de diretórios, percorrendo a árvore de cima para baixo ou de baixo para cima.
list_dir = [x[0] for x in os.walk(directory)]
list_dir = list_dir[1:]
list_name = []
for dirnames in list_dir:
  list_filenames = [x[2] for x in os.walk(dirnames)][0]
  for filenames in list_filenames:
    # Se a extenção do aqruivo for .xml
    if filenames.endswith(".xml"):
      list_name.append(filenames)
      tree = ET.parse(dirnames + '/' + filenames)
      root = tree.getroot()
      list_xml_freq = []
      list_xml_phAngle = []
      list_xml_power = []
      list_xml_reacPower = []
      list_xml_rmsCur = []
      list_xml_rmsVolt = []
      for child in root:
        if child.tag == 'signalCurve':
          for child_2 in child:
            list_xml_freq.append(float(child_2.get('freq')))
            list_xml_phAngle.append(float(child_2.get('phAngle')))
            list_xml_power.append(float(child_2.get('power')))
            list_xml_reacPower.append(float(child_2.get('reacPower')))
            list_xml_rmsCur.append(float(child_2.get('rmsCur')))
            list_xml_rmsVolt.append(float(child_2.get('rmsVolt')))
      check_xml = True
      # if (list_xml_freq != list_mat_freq):
      #   print(filenames)
      # if (list_xml_phAngle != list_mat_phAngle):
      #   print(filenames)
      # if (list_xml_power != list_mat_power):
      #   print(filenames)
      # if (list_xml_reacPower != list_mat_reacPower):
      #   print(filenames)
      # if (list_xml_rmsCur != list_mat_rmsCur):
      #   print(filenames)
      # if (list_xml_rmsVolt != list_mat_rmsVolt):
      #   print(filenames)
      print(list_xml_phAngle)
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
        print(filenames)

      # print('ok')
      # if (filenames[-5] != child.get('session')):
      #   child.set('session', filenames[-5])
      #   tree.write(dirnames + '/' + filenames)
      print(list_mat_phAngle)
# for i in range(0,len(list_db)):
#    print(list_db[i] + '\t' + list_name[i])

#  OBS: comparar arquivo .xml com arquivo .mat para obter resultado.