import tensorflow as tf

# Path to your H5 model
h5_model_path = "/Users/gungdeari/Project/Ageman-capstone/ageman_model.h5"

# Load the Keras model from the H5 file
model = tf.keras.models.load_model(h5_model_path)

# Save the model as a TensorFlow SavedModel
saved_model_dir = "/Users/gungdeari/Project/Ageman-capstone/saved_model"
tf.saved_model.save(model, saved_model_dir)