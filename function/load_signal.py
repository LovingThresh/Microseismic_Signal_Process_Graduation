import numpy as np
import pandas as pd
import os
import shutil


def get_filepath(parent_path, class_number=0):  # class_number=1指的是微震
    """
    获取父路径的子文件路径
    :param parent_path: 父路径
    :param class_number: 文件类别
    :return: 某一路径下的所有.mwf文件路径列表
    """
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
    """
    加载数据
    :param filepath: 数据文件路径
    :return: raw_signal (ndarray)
    """
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
             datafile_path=r'C:\Users\liuye\Desktop\dataset_for_graduation\Microseism'):
    """
    复制文件
    :param data_filename_list: 需要复制的文件名列表
    :param train_dir: 指定Train文件夹路径
    :param validation_dir: 指定Validation文件夹路径
    :param test_dir: 指定Test文件夹路径
    :param label: 标签
    :param datafile_path: 数据文件路径，源路径
    :return: Copy
    """
    os.chdir(datafile_path)
    fileList = os.listdir(datafile_path)
    # fileList = data_filename_list
    length = len(fileList)
    for i in fileList[:int(length * 0.7)]:
        shutil.copyfile(i, r'{}/{}/{}'.format(train_dir, label, i))
    for i in fileList[int(length * 0.7):int(length * 0.9)]:
        shutil.copyfile(i, r'{}/{}/{}'.format(validation_dir, label, i))
    for i in fileList[int(length * 0.9):]:
        shutil.copyfile(i, r'{}/{}/{}'.format(test_dir, label, i))

    return 0


def creat_train_file():
    """
    创建文件夹
    :return:
    """
    os.mkdir(r'L:\dataset_for_graduation\Train')
    os.mkdir(r'L:\dataset_for_graduation\Validation')
    os.mkdir(r'L:\dataset_for_graduation\Test')
    os.mkdir(r'L:\dataset_for_graduation\Train\Microseism')
    os.mkdir(r'L:\dataset_for_graduation\Validation\Microseism')
    os.mkdir(r'L:\dataset_for_graduation\Train\Demolition')
    os.mkdir(r'L:\dataset_for_graduation\Validation\Demolition')
    os.mkdir(r'L:\dataset_for_graduation\Test\Demolition')
    os.mkdir(r'L:\dataset_for_graduation\Test\Microseism')


def file_filter(f, mask):
    """
    文件过滤器
    :param f: 文件
    :param mask: Mask条件
    :return: 满足条件的文件
    """
    if mask in f:
        return True
    else:
        return False


def move_to_path(data_path, label='Demolition'):
    """
    组合copyfile函数与file_filter函数，实现文件移动至指定路径
    :param data_path: 源文件
    :param label: 标签
    :return: Move file
    """
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
        copyfile(each_type_list, train_dir, validation_dir, test_dir, label, data_path)
