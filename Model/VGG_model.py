# 使用VGG16训练模型
from keras.applications import VGG16
from keras import models
from keras import layers


def set_VGG16_model():
    # 设置卷积网络基础VGG16
    conv_base = VGG16(weights='imagenet',
                      include_top=False,
                      input_shape=(224, 224, 3))
    # 组建网络
    model = models.Sequential()
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.25))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    # 解冻VGG16卷积的最后几层

    set_trainable = False
    for layer in conv_base.layers:
        if layer.name == 'block5_conv1':
            set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False

    return model
