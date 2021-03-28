# 测试性能
import re
from function.load_signal import *
from function.Data_flow_Plot import *


def main():
    # 指定文件夹
    raw_data_filepath = r'L:\test'
    each_datafile_path_list = get_filepath(raw_data_filepath)
    for filepath in each_datafile_path_list:
        raw_data = load_signal(filepath)
        filename = re.split(r'[\\.]', filepath)[-2]

        flow_data(raw_data, filename=filename, label='Microseism')


if __name__ == '__main__':
    main()
