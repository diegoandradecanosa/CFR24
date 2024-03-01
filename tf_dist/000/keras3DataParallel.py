import os

# The distribution API is only implemented for the JAX backend for now.
#os.environ["KERAS_BACKEND"] = "jax"
os.environ["KERAS_BACKEND"] = "jax"

import keras
from keras import layers
#import tensorflow as tf
import jax
import numpy as np
from tensorflow import data as tf_data  # For dataset input.

# Retrieve the local available gpu devices.
devices = jax.devices("gpu")  

# Create DataParallel with list of devices.
# As a shortcut, the devices can be skipped,
# and Keras will detect all local available devices.
# E.g. data_parallel = DataParallel()
data_parallel = keras.distribution.DataParallel(devices=devices)

# Or you can choose to create DataParallel with a 1D `DeviceMesh`.
mesh_1d = keras.distribution.DeviceMesh(
    shape=(2,), axis_names=["data"], devices=devices
)
data_parallel = keras.distribution.DataParallel(device_mesh=mesh_1d)

inputs = np.random.normal(size=(128, 28, 28, 1))
labels = np.random.normal(size=(128, 10))
dataset = tf_data.Dataset.from_tensor_slices((inputs, labels)).batch(16)

# Set the global distribution.
keras.distribution.set_distribution(data_parallel)

# Note that all the model weights from here on are replicated to
# all the devices of the `DeviceMesh`. This includes the RNG
# state, optimizer states, metrics, etc. The dataset fed into `model.fit` or
# `model.evaluate` will be split evenly on the batch dimension, and sent to
# all the devices. You don't have to do any manual aggregration of losses,
# since all the computation happens in a global context.
inputs = layers.Input(shape=(28, 28, 1))
y = layers.Flatten()(inputs)
y = layers.Dense(units=200, use_bias=False, activation="relu")(y)
y = layers.Dropout(0.4)(y)
y = layers.Dense(units=10, activation="softmax")(y)
model = keras.Model(inputs=inputs, outputs=y)

model.compile(loss="mse")
model.fit(dataset, epochs=3)
model.evaluate(dataset)

