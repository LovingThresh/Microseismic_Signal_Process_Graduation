from keras.preprocessing.image import ImageDataGenerator


def Image_Data_Generator(train_dir, validation_dir):
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

    return train_generator, validation_generator