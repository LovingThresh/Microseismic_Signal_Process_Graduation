# 测试 2 阶段：
# 转移文件，并进行VGG16的模型初试，构建ResNet网络模型
# 构建特征矩阵，进行相应的计算
from function.load_signal import *


def main():

    # creat_train_file() 已经创建
    data_path = r'C:\Users\liuye\Desktop\dataset_for_graduation\Demolition'
    move_to_path(data_path, label='Demolition')

    return 0


if __name__ == '__main__':
    main()