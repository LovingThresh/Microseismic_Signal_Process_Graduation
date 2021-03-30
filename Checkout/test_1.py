# 测试 1 阶段：
# 测试性能,将所有的数据扩充转换成图片存储在相应的文件夹中

import re
from function.load_signal import *
from function.Data_flow_Plot import *


def main():
    # 指定文件夹
    raw_data_filepath = r'L:\sj'
    each_datafile_path_list = get_filepath(raw_data_filepath)
    for filepath in each_datafile_path_list:
        raw_data = load_signal(filepath)
        filename = re.split(r'[\\.]', filepath)[-2]

        flow_data(raw_data, filename=filename, label='Demolition')


if __name__ == '__main__':
    main()

# 至此将所有的数据扩充转换成图片存储在相应的文件夹中
