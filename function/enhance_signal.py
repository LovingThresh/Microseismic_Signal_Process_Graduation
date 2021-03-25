import numpy as np
import matlab.engine


# 给信号添加指定SNR的高斯噪音
def awgn(x, snr, seed=7):
    """
    加入高斯白噪音
    :param x: 原始信号 Signal
    :param snr: 信噪比
    :param seed: 随机种子
    :return: 加入噪音后的信号
    """
    np.random.seed(seed)  # 设置随机种子
    snr = 10 ** (snr / 10.0)
    x_power = np.sum(x ** 2) / len(x)
    n_power = x_power / snr
    noise = np.random.randn(len(x)) * np.sqrt(n_power)

    return x + noise


# 对信号进行移位
def shift_signal(signal, change_length):
    """
    对输入信号signal进行change_length长度的移位，剪切前段信号，拼接至末尾
    :param signal: 原始信号
    :param change_length: 信号剪切长度
    :return:
    """
    section = signal[0:change_length]
    change_signal = signal[change_length + 1:] + section

    return change_signal


# 对信号进行翻转f(t) -> f(-t)
def reversal_signal(signal):
    return -signal


# 对信号进行降噪处理
def denoise_signal(signal):
    """
    调用MatLab中的WienerScalar96函数对信号进行降噪
    :param signal: 原始信号
    :return: 降噪后的信号
    """
    slice_signal = signal[:, :1000]
    enhance_signal = np.concatenate([slice_signal, slice_signal, slice_signal, slice_signal, signal], axis=1)
    np.savetxt('enhance_signal.csv', enhance_signal, delimiter=',')
    function = matlab.engine.start_matlab(async=True)
    data = function.result()
    data = data.csvread('enhance_signal.csv')
    function_2 = matlab.engine.start_matlab(async=True)
    a = function_2.result()
    fs = 10000
    IS = 0.7
    result = a.WienerScalart96(data, fs, IS)# 此处不能输入数字，否则会报错
    number = len(result) - signal.shape[1]
    result = result[number:]

    return result


