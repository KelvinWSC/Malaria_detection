#%%
from pathlib import Path
from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import callbacks

#%%
x = []
y = []

for i in (Path('cell_images')/'Parasitized').glob('*.png'):
    x.append(image.img_to_array(image.load_img(i, target_size=(64,64))))
    y.append(1)

for i in (Path('cell_images')/'Uninfected').glob('*.png'):
    x.append(image.img_to_array(image.load_img(i, target_size=(64,64))))
    y.append(0)

x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=28)
x_train = x_train / 255.
x_test = x_test / 255.

# %%
model = Sequential()
model.add(Conv2D(40,kernel_size=(3,3),activation='relu', input_shape=(64,64,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(30,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(20,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(10,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
opt = keras.optimizers.Adam()
model.compile(optimizer=opt, loss=tf.keras.losses.binary_crossentropy, metrics=['accuracy'])
#%%
final_model = model.fit(x_train, y_train, batch_size=20, epochs=20, validation_data=(x_test, y_test), callbacks=[callbacks.EarlyStopping(monitor='val_loss',min_delta=0.1, patience=5)])

#%%
plt.plot( list(range(1, len(final_model.history['accuracy'])+1)), final_model.history['accuracy'] )
plt.plot( list(range(1, len(final_model.history['accuracy'])+1)), final_model.history['val_accuracy'] )
plt.legend(('Training Accuracy', 'Validation Accuracy'))
plt.ylabel('Accuracy')
plt.xlabel('epoch')
plt.show()
