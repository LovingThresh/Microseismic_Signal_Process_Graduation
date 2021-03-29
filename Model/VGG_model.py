# 使用VGG16训练模型
from keras.applications import VGG16
from keras import models
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from function.Plot_result import plot
from callback.Callback import set_callbacks
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

train_dir = r''
validation_dir = r''

# 设置卷积网络基础VGG16
conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(224, 224, 3))
# 组建网络
model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
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

# 设置图像生成器的参数
train_datagen = ImageDataGenerator(rescale=1. / 255)
validation_datagen = ImageDataGenerator(rescale=1. / 255)

# 数据生成器
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=20,  # 注意batch_size的值，要相对应
    class_mode='binary'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    batch_size=20,  # 注意batch_size的值，要相对应
    class_mode='binary'
)

# 编译model
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=2e-5),
              metrics=['acc'])

callbacks, logdir = set_callbacks()

history = model.fit_generator(
    train_generator,
    epochs=30,
    shuffle=True,
    callbacks=callbacks,
    validation_data=validation_generator,
)

# 打印结果

plot(history)
