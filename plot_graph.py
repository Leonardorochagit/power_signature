import matplotlib.pyplot
import numpy as np


def initialize(values):
  temp = np.arange(0, 359, 1).tolist()

  matplotlib.pyplot.plot(temp, values)
  matplotlib.pyplot.show()
