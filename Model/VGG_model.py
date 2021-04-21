# 使用VGG16训练模型
from keras.applications import VGG16
from keras import models
from keras import layers


def set_VGG16_model():
    # 设置卷积网络基础VGG16
    conv_base = VGG16(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    conv_base.trainable = True
    # 组建网络
    model = models.Sequential()
    model.add(layers.GaussianNoise(0.125, input_shape=(224, 224, 3)))
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.GaussianNoise(0.25))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))

    # 解冻VGG16卷积的最后几层
    set_trainable = False
    for layer in conv_base.layers:
        if layer.name == 'block4_conv1':
            set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False

    return model
# model.load_weights(r'')