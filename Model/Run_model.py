from keras import optimizers
from function.Plot_result import plot


def Run_model(model, train_generator, validation_generator, callbacks):
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=2e-5),
                  metrics=['acc'])

    history = model.fit_generator(train_generator,
                                  epochs=30,
                                  shuffle=True,
                                  callbacks=callbacks,
                                  validation_data=validation_generator)

    plot(history)
