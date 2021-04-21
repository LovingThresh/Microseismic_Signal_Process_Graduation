from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, BatchNormalization, MaxPool2D, Flatten, GaussianNoise

def set_my_Model():

    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(7, 7), padding='Same', activation='relu', input_shape=(224, 224, 3)))
    model.add(BatchNormalization())
    model.add(GaussianNoise(0.25))
    model.add(Conv2D(filters=32, kernel_size=(7, 7), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(GaussianNoise(0.25))
    model.add(Conv2D(filters=64, kernel_size=(5, 5), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=64, kernel_size=(5, 5), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    '''
    model.add(Conv2D(filters=256, kernel_size=(3, 3), padding='Same', activation='relu', input_shape=(224, 224, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=256, kernel_size=(3, 3), padding='Same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    '''
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    return model














