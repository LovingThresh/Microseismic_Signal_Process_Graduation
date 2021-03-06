from keras.preprocessing.image import ImageDataGenerator


def Image_Data_Generator(train_dir, validation_dir, test_dir):
    # 设置图像生成器的参数
    train_datagen = ImageDataGenerator(rescale=1. / 255)
    validation_datagen = ImageDataGenerator(rescale=1. / 255)
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    # 数据生成器
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=30,  # 注意batch_size的值，要相对应
        class_mode='binary'
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=30,  # 注意batch_size的值，要相对应
        class_mode='binary'
    )

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        class_mode='binary'
    )

    return train_generator, validation_generator, test_generator



