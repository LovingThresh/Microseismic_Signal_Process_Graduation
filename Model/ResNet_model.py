from keras.applications import ResNet50
from keras import models
from keras import layers


def set_ResNet_model():
    conv_base = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    conv_base.trainable = True

    # 组建网络
    model = models.Sequential()
    model.add(layers.GaussianNoise(0.125, input_shape=(224, 224, 3)))
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))

    # 解冻ResNet50的最后几层
    set_trainable = False
    for layer in conv_base.layers:
        if layer.name == 'conv5_block1_1_conv':
            set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False

    return model
