from keras import optimizers
from function.Plot_result import plot


def Run_model(model, train_generator, validation_generator, test_generator, callbacks):
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=1e-5),
                  metrics=['acc'])

    history = model.fit_generator(train_generator,
                                  # steps_per_epoch=1200,
                                  epochs=100,
                                  shuffle=True,
                                  callbacks=callbacks,
                                  validation_data=validation_generator,
                                  validation_steps=25)

    plot(history)

    # 测试集结果
    loss, accuracy = model.evaluate(test_generator, batch_size=32, verbose=1)
    print('测试集的损失与准确率分别为{}，{}'.format(float('%.4f' % loss), float('%.4f' % accuracy)))

    return model