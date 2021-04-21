# 测试 3 阶段：
# 对构建的VGG16模型与ResNet模型进行性能测试
# 对超参数进行调整，获取最佳效果

from Model.ResNet_model18 import *
from Model.VGG_model import *
from Model.VGG16_model import *
from Model.ResNet_model import *
from Model.my_Model import *
from Model.Run_model import *
from function.Image_generator import Image_Data_Generator
from callback.Callback import set_callbacks

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)


def main():
    # 创建model
    # run_model_1 = ResNet18([2, 2, 2, 2])
    run_model_2 = set_VGG16_model()
    # run_model_3 = VGG16()
    # run_model_4 = set_ResNet_model()
    # run_model_5 = set_my_Model()


    # 获取train_data与validation_data
    train_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Train'
    validation_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Validation'
    test_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Test'
    train_generator, validation_generator, test_generator = Image_Data_Generator(train_dir, validation_dir, test_dir)

    # 获取callback函数
    callbacks, logdir = set_callbacks()

    # 运行程序并得出训练曲线
    # Run_model(run_model_1, train_generator, validation_generator, test_generator, callbacks)
    Run_model(run_model_2, train_generator, validation_generator, test_generator, callbacks)
    # Run_model(run_model_3, train_generator, validation_generator, test_generator, callbacks)
    # Run_model(run_model_4, train_generator, validation_generator, test_generator, callbacks)
    # Run_model(run_model_5, train_generator, validation_generator, test_generator, callbacks)


def test_function():
    # 获取train_data与validation_data
    train_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Train'
    validation_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Validation'
    test_dir = r'C:\Users\liuye\Desktop\dataset_for_graduation\Test'
    train_generator, validation_generator, test_generator = Image_Data_Generator(train_dir, validation_dir, test_dir)
    filepath = r'I:\PycharmProjects\Microseismic_Signal_Process_Graduation\Checkout\callbacks\ep025-val_loss0.098-val_acc0.972.h5'
    model = set_my_Model()
    model = models.load_model(filepath)
    loss, accuracy = model.evaluate(test_generator, batch_size=20, verbose=1)
    print('测试集的损失与准确率分别为{}，{}'.format(float('%.4f' % loss), float('%.4f' % accuracy)))


if __name__ == '__main__':
    main()