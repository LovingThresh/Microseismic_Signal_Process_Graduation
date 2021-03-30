from keras import optimizers
from function.Plot_result import plot


def Run_model(model, train_generator, validation_generator, test_generator, callbacks):
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=2e-5),
                  metrics=['acc'])

    history = model.fit(train_generator,
                        epochs=3,
                        shuffle=True,
                        callbacks=callbacks,
                        validation_data=validation_generator)

    plot(history)

    # 测试集结果
    loss, accuracy = model.evaluate(test_generator, bathsize=10, verbose=1)
    print('测试集的损失与准确率分别为{}，{}'.format(loss, accuracy))
