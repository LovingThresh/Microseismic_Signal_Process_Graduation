import os
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping


def set_callbacks():
    """设置回调函数"""

    # 1. 有关回调函数的设置（callbacks）
    logdir = os.path.join('callbacks')
    print(logdir)
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    filepathAcc = os.path.join(logdir, 'ep{epoch:03d}-val_loss{val_loss:.3f}-val_acc{val_acc:.3f}.h5')
    callbacks = [ModelCheckpoint(filepathAcc, monitor='val_acc', save_best_only=True, save_freq='epoch'),
                 ReduceLROnPlateau(factor=0.5, patience=10),
                 EarlyStopping(monitor='val_acc', patience=20, mode='max')
                 ]

    return callbacks, logdir
