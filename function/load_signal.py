import numpy as np
import pandas as pd
import os
import shutil


def get_filepath(parent_path, class_number=0):  # class_number=1指的是微震
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


def copyfile(data_filename_list, train_dir, validation_dir, test_dir, label='Microseism',
             datafile_path=r'L:\dataset_for_graduation\Microseism'):
    os.chdir(datafile_path)
    fileList = data_filename_list
    length = len(fileList)
    for i in fileList[:int(length * 0.7)]:
        shutil.copyfile(i, r'{}/{}/{}'.format(train_dir, label, i))
    for i in fileList[int(length * 0.7):int(length * 0.9)]:
        shutil.copyfile(i, r'{}/{}/{}'.format(validation_dir, label, i))
    for i in fileList[int(length * 0.9):]:
        shutil.copyfile(i, r'{}/{}/{}'.format(test_dir, label, i))

    return 0


def creat_train_file():
    os.mkdir(r'L:\dataset_for_graduation\Train')
    os.mkdir(r'L:\dataset_for_graduation\Validation')
    os.mkdir(r'L:\dataset_for_graduation\Test')
    os.mkdir(r'L:\dataset_for_graduation\Train\Microseism')
    os.mkdir(r'L:\dataset_for_graduation\Validation\Microseism')
    os.mkdir(r'L:\dataset_for_graduation\Train\Demolition')
    os.mkdir(r'L:\dataset_for_graduation\Validation\Demolition')


def file_filter(f, mask):
    if mask in f:
        return True
    else:
        return False


def move_to_path(data_path, label='Microseism', datafile_path=r'L:\dataset_for_graduation\Microseism'):
    file_list = os.listdir(data_path)
    raw_data_list = [raw_data_file for raw_data_file in file_list if file_filter(raw_data_file, 'raw_data')]
    enhance_data_1_list = [enhance_data_1_file
                           for enhance_data_1_file in file_list if file_filter(enhance_data_1_file, 'enhance_data_1')]
    enhance_data_2_list = [enhance_data_2_file
                           for enhance_data_2_file in file_list if file_filter(enhance_data_2_file, 'enhance_data_2')]
    enhance_data_3_list = [enhance_data_3_file
                           for enhance_data_3_file in file_list if file_filter(enhance_data_3_file, 'enhance_data_3')]
    enhance_data_4_list = [enhance_data_4_file
                           for enhance_data_4_file in file_list if file_filter(enhance_data_4_file, 'enhance_data_4')]
    for each_type_list in [raw_data_list, enhance_data_1_list, enhance_data_2_list, enhance_data_3_list,
                           enhance_data_4_list]:
        train_dir = r'L:\dataset_for_graduation\Train'
        validation_dir = r'L:\dataset_for_graduation\Validation'
        test_dir = r'L:\dataset_for_graduation\Test'
        copyfile(each_type_list, train_dir, validation_dir, test_dir, label, datafile_path)
