import numpy as np
import pandas as pd
import os


def get_filepath(parent_path, class_number=0):
    datafile_name = os.listdir(parent_path)
    datafile_path = os.path.join(parent_path, datafile_name[class_number])
    each_file_names = os.listdir(datafile_path)
    each_datafile_path_list = []
    for each_file_name in each_file_names:
        if os.path.splitext(each_file_name)[1] == '.mwf':
            each_datafile_path = os.path.join(datafile_path, each_file_name)
            each_datafile_path_list.append(each_datafile_path)

    return each_datafile_path_list


def load_signal(filepath):
    data = pd.DataFrame(pd.read_table(filepath, skiprows=11, delimiter=',', header=None, dtype='float'))
    data = data.fillna(0)
    number_data = np.asarray(data)
    [_, c_size] = number_data.shape
    if c_size == 3:
        data = np.asarray([number_data[:, 0] + number_data[:, 1] + number_data[:, 2]])
    else:
        data = number_data

    return data
