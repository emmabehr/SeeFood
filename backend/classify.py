import pickle
import cv2
import numpy as np
import tensorflow as tf

import ml_constants

def prepareImageFromBytes(image_bytes):
    #image_array = np.fromstring(image_bytes, np.uint8)
    #image = cv2.imdecode(image_array, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (ml_constants.IMAGE_HEIGHT, ml_constants.IMAGE_WIDTH), interpolation = cv2.INTER_AREA)
    image = np.array(image)
    image = image.astype('float32')
    image = image / 255

    return image

def loadModel(model_path):
    model = tf.keras.models.load_model(model_path)
    model.summary()
    return model

def predict(image_bytes):
    image = prepareImageFromBytes(image_bytes)
    model = loadModel(ml_constants.MODEL_PATH)
    #x=np.array(image, np.float32)

    x = tf.keras.preprocessing.image.img_to_array(image)
    image_batch = np.expand_dims(x, axis=0)
    
    predictions = model.predict(image_batch)
    #predictions = model.predict(x)

    ##processed_image = preprocess_input(image_batch, mode='caffe')

    return predictions

def getLabels():
    class_names = pickle.loads(open(ml_constants.CLASSES_PATH, "rb").read())
    return class_names

def getPredictedLabel(label_index):
    class_names = getLabels()
    label = class_names[label_index]
    return label

def classify(image):
    predictions = predict(image)
    print(predictions)
    predictioned = np.argmax(predictions)
    print(predictioned)

    #prediction = tf.keras.applications.imagenet_utils.decode_predictions(predictions, top=1)
    classification = getPredictedLabel(predictioned)
    print(classification)
    return classification