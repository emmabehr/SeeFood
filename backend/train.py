import os #module to call operating system, use it to access files
import pickle #save and load off python object, serialise/deseralise. 
import cv2 #an image manupulation library.  Be able to prepare images formating for neural network 
import numpy as np # (as is just a shortened name, that you can choose) numpy module to handle numbers of the processed image  (numerical computing)
import tensorflow as tf #tensor is the machine learning library 

import ml_constants #to define variables that are used in multipe files (between the training.py and classiy.py) its so i can have the variables define in ml_constants 
#and it updates both training and classify variables with those names

# defining method that takes a 
def create_dataset(root_images_directory):
	absolute_root_path = os.path.abspath(root_images_directory)
	print(absolute_root_path)
	image_data_array=[]
	class_names=[]
#
	for class_directory in os.listdir(absolute_root_path):
		print(class_directory)
		for image_file in os.listdir(os.path.join(absolute_root_path, class_directory)):
			try:
				image_path = os.path.join(absolute_root_path, class_directory, image_file)
				image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
				image = cv2.resize(image, (ml_constants.IMAGE_HEIGHT, ml_constants.IMAGE_WIDTH), interpolation = cv2.INTER_AREA)
				image = np.array(image)
				image = image.astype('float32')
				image = image / 255

				image_data_array.append(image)

				class_names.append(class_directory)
			except:
				print("failed to process image {}".format(image_path))

	return image_data_array, class_names

# extract the image array and class name
# declare two variables and to set the values call the function create data set, with the parameter which is the path to the image folder.
image_data, class_names = create_dataset('images')

target_dict = {k: v for v, k in enumerate(np.unique(class_names))}
target_classes = [k for k in target_dict]
f = open(ml_constants.CLASSES_PATH, "wb")
f.write(pickle.dumps(target_classes))
f.close()
target_val =  [target_dict[class_names[i]] for i in range(len(class_names))]
print(len(target_classes))

model = tf.keras.Sequential(
	[
		tf.keras.layers.InputLayer(input_shape=(ml_constants.IMAGE_HEIGHT,ml_constants.IMAGE_WIDTH, 3)),
		tf.keras.layers.Conv2D(filters=16, kernel_size=3, strides=(2, 2), activation='relu'),
		tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=(2, 2), activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Flatten(),
        #tf.keras.layers.Dense(32, activation=tf.keras.activations.softmax)
        tf.keras.layers.Dense(len(target_classes), activation=tf.keras.activations.softmax)
	]
)

print(model.summary())

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x=np.array(image_data, np.float32), y=np.array(list(map(int,target_val)), np.float32), epochs=10)

model.save(ml_constants.MODEL_PATH)