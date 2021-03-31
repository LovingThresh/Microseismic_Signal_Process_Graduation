import os
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping


def set_callbacks():
    """设置回调函数"""

    # 1. 有关回调函数的设置（callbacks）
    logdir = os.path.join('callbacks')
    print(logdir)
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    output_model_file = os.path.join(logdir, 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}-val_acc{'
                                             'val_acc:.3f}.h5')
    callbacks = [
        ModelCheckpoint(output_model_file, save_best_only=True, save_freq='epoch'),
        ReduceLROnPlateau(factor=0.5, patience=3),
        EarlyStopping(min_delta=1e-3, patience=10)
    ]

    return callbacks, logdir