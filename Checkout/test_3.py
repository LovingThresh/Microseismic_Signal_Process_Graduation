from Model.ResNet_model import *
from Model.VGG_model import *
from Model.Run_model import *
from function.Image_generator import Image_Data_Generator
from callback.Callback import set_callbacks

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)


def main():
    # 创建model
    # run_model_1 = ResNet18([2, 2, 2, 2])
    run_model_2 = set_VGG16_model()

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


if __name__ == '__main__':
    main()