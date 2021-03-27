import numpy as np
import pandas as pd


def load_signal(filepath):
    data = pd.DataFrame(pd.read_table(filepath, skiprows=11, delimiter=',', header=None, dtype='float'))
    number_data = np.asarray(data)
    [i_size, c_size] = number_data.shape
    if c_size == 3:
        data = np.asarray([number_data[:, 0] + number_data[:, 1] + number_data[:, 2]])
    else:
        data = number_data

    return data
