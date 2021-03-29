# load_signal 获取信号后,经过enhance_signal之后flow_to图片,并存储至相应的文件夹
from function.Plot_CWT import function_CWT_p2m
from function import enhance_signal


def flow_data(raw_data, filename, label):
    filename_0 = 'raw_data' + '_' + filename
    label = label
    function_CWT_p2m(raw_data, filename=filename_0, label=label)  # raw_data -->  CWT图片

    # 接下来flow_enhance_data
    enhance_signal_1 = enhance_signal.awgn(raw_data, snr=0.2, seed=7)  # （添加噪音）
    filename_1 = 'enhance_data_1' + '_' + filename
    function_CWT_p2m(enhance_signal_1, filename=filename_1, label=label)

    enhance_signal_2 = enhance_signal.shift_signal(raw_data, change_length=1000)  # （移位信号）
    filename_2 = 'enhance_data_2' + '_' + filename
    function_CWT_p2m(enhance_signal_2, filename=filename_2, label=label)

    enhance_signal_3 = enhance_signal.reversal_signal(raw_data)  # （翻转信号）
    filename_3 = 'enhance_data_3' + '_' + filename
    function_CWT_p2m(enhance_signal_3, filename=filename_3, label=label)

    '''
    enhance_signal_4 = enhance_signal.denoise_signal(raw_data)  # （降噪信号）
    filename_4 = 'enhance_data_4' + '_' + filename
    function_CWT_p2m(enhance_signal_4, filename=filename_4, label=label)
    '''

    # 至此，数据拓展可以以CWT图片的形式保存在文件夹中