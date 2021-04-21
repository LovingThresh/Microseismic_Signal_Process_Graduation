import matplotlib.pyplot as plt


plt.switch_backend('TKAgg')

def plot(history):
    """
    打印结果
    :param history:
    :return:
    """
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = [i for i in range(1, len(loss) + 1)]

    plt.figure(1)

    plt.plot(epochs, loss, 'bo', label="Training loss")
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()

    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = [i for i in range(1, len(acc) + 1)]

    plt.figure(2)

    plt.plot(epochs, acc, 'bo', label="Training accuracy")
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.show()