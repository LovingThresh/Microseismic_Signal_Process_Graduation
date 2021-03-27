# 启动MATLAB引擎绘制CWT连续小波变换图像
import matlab.engine
import numpy as np


def function_CWT_p2m(signal, filename='test', label='Microseism'):  # 此处导入数据时应该注意filename的设置
    np.savetxt('signal.csv', signal, delimiter=',')  # 这是是为了数据能够相互使用
    function = matlab.engine.start_matlab()
    signal = function.csvread('signal.csv')
    function_CWT = matlab.engine.start_matlab(async=True)
    filename = 'test'
    label = 'Microseism'
    function_CWT = function_CWT.result()
    a = function_CWT.helperCreateRGBfromTFforMicroseism(signal, filename, label)