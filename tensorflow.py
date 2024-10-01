import tensorflow as tf
from tensorflow.keras import layers, models

# Define the encoder
def build_encoder(input_dim, encoding_dim):
    encoder = models.Sequential()
    encoder.add(layers.InputLayer(input_shape=(input_dim,)))
    encoder.add(layers.Dense(encoding_dim, activation='relu'))
    return encoder

# Define the decoder
def build_decoder(encoding_dim, input_dim):
    decoder = models.Sequential()
    decoder.add(layers.InputLayer(input_shape=(encoding_dim,)))
    decoder.add(layers.Dense(input_dim, activation='sigmoid'))
    return decoder

# Define the autoencoder
input_dim = 784  # Example for MNIST dataset (28x28 images)
encoding_dim = 32

encoder = build_encoder(input_dim, encoding_dim)
decoder = build_decoder(encoding_dim, input_dim)

autoencoder = models.Sequential([encoder, decoder])
autoencoder.compile(optimizer='adam', loss='mse')

# Example data for training
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, input_dim) / 255.0
x_test = x_test.reshape(-1, input_dim) / 255.0

# Train the autoencoder
autoencoder.fit(x_train, x_train, epochs=50, batch_size=256, shuffle=True, validation_data=(x_test, x_test))
