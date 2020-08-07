import csv
import os

def create_table():
  c = csv.writer(open("db_elet.csv", "w"))

  c.writerow(["Eletro", "phAngle_min", "phAngle_max", "Freq_min", "Freq_max", "ReactPower_min", "ReactPower_max", "Power_min", "Power_max", "Volts_min", "Volts_max", "Cur_min", "Cur_max"])

def write_row(name, angle_min, angle_max, freq_min, freq_max, react_power_min, react_power_max, power_min, power_max, volts_min, volts_max, cur_min, cur_max):
  c = csv.writer(open("db_elet.csv", "w"))
  c.writerow([(name, angle_min, angle_max, freq_min, freq_max, react_power_min, react_power_max, power_min, power_max, volts_min, volts_max, cur_min, cur_max)])