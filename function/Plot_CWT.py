# 启动MATLAB引擎绘制CWT连续小波变换图像
import matlab.engine
import numpy as np


def function_CWT_p2m(signal, filename='test', label='Microseism'):  # 此处导入数据时应该注意filename的设置
    """
    将signal转换成CWT图片
    :param signal: 从load_signal与enhance得到的signal(ndarray)
    :param filename: 便于命名，识别文件信息
    :param label: 标签_Microseism_Demolition
    :return: 无
    """
    np.savetxt(r'I:\PycharmProjects\Microseismic_Signal_Process_Graduation\signal_filename.csv', signal, delimiter=',')
    # 这是是为了数据能够相互使用
    function = matlab.engine.start_matlab()
    signal = function.csvread(r'I:\PycharmProjects\Microseismic_Signal_Process_Graduation\signal_filename.csv')
    function.exit()
    function_CWT = matlab.engine.start_matlab()
    function_CWT.helperCreateRGBfromTFforMicroseism(signal, filename, label)
    function_CWT.exit()