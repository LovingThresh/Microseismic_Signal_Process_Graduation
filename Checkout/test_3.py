from Model.ResNet_model import *
from Model.VGG_model import *
from Model.Run_model import *
from function.Image_generator import Image_Data_Generator
from callback.Callback import set_callbacks

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)


def main():
    run_model_1 = ResNet18([2, 2, 2, 2])
    run_model_2 = set_VGG16_model()

    train_dir = r''
    validation_dir = r''
    train_generator, validation_generator = Image_Data_Generator(train_dir, validation_dir)

    callbacks, logdir = set_callbacks()

    Run_model(run_model_1, train_generator, validation_generator, callbacks)
    Run_model(run_model_2, train_generator, validation_generator, callbacks)


if __name__ == '__main__':
    main()