import tensorflow as tf
from keras import Model
from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, Activation, Flatten, Dense


class ResnetBlock(Model):

    def __init__(self, filters, strides=1, residual_path=False):
        super(ResnetBlock, self).__init__()
        self.filters = filters
        self.strides = strides
        self.residual_path = False

        self.c1 = Conv2D(filters, (3, 3), strides=strides, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')

        self.c2 = Conv2D(filters, (3, 3), strides=strides, padding='same', use_bias=False)
        self.b2 = BatchNormalization()

        # 接入Residual_Path
        if residual_path:
            self.down_c1 = Conv2D(filters, (3, 3), strides=strides, padding='same', use_bias=False)
            self.down_b1 = BatchNormalization()

        self.a2 = Activation('relu')

    def call(self, inputs, mask=None):
        residual = inputs
        # 正常路径
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)

        x = self.c2(x)
        y = self.b2(x)

        if self.residual_path:
            residual = self.down_c1(inputs)
            residual = self.down_b1(residual)

        out = self.a2(y + residual)

        return out


class ResNet18(Model):
    def __init__(self, block_list, initial_filters=64):
        super(ResNet18, self).__init__()
        self.num_block = len(block_list)
        self.block = block_list
        self.out_filters = initial_filters
        self.c1 = Conv2D(self.out_filters, (3, 3), strides=1, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.blocks = Sequential()

        # 构建ResNet网络结构
        for block_id in range(len(block_list)):  # 第几个resnet block
            for layer_id in range(block_list[block_id]):  # 第几个卷积层

                if block_id != 0 and layer_id == 0:  # 对除第一个block以外的每个block的输入进行下采样
                    block = ResnetBlock(self.out_filters, strides=2, residual_path=True)
                else:
                    block = ResnetBlock(self.out_filters, residual_path=False)
                self.blocks.add(block)  # 将构建好的block加入resnet
            self.out_filters *= 2  # 下一个block的卷积核数是上一个block的2倍
        self.p1 = tf.keras.layers.GlobalAveragePooling2D()
        self.f1 = Flatten()
        self.d1 = Dense(1, activation='sigmoid', kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, inputs, mask=None):
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)

        x = self.blocks(x)

        x = self.p1(x)
        x = self.f1(x)
        x = self.d1(x)

        return x


