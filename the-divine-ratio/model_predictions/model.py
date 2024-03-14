
# coding: utf-8

# In[60]:

# Importing tensorflow
    
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator, load_img

# In[61]:

#Choosing an image to predict 

import easygui
print("Choose an Image")
path = easygui.fileopenbox()
print('Location: ',path)

# Copying the image chosen by the user to the directory from where the algorithm 
# looks for images

import shutil
dst = "the_images_go_inside_the_subfolder/the_images_go_here/"
shutil.copy(path, dst, follow_symlinks=True)


test_data_dir = "test"


# In[62]:


# Rescaling the images

test_datagen =  ImageDataGenerator(
    rescale=1./255
)


# In[63]:

# Defining the image proportions

img_height = 224
img_width = 224
batch_size = 32


# In[64]:

# Importing the trained model

import tensorflow as tf
model = tf.keras.models.load_model("ratio_aug1.h5")



# In[95]:


# Defining the directory from where the algorithm looks for images to predict

val1_data_dir = "the_images_go_inside_the_subfolder"
val1_generator = test_datagen.flow_from_directory(
    val1_data_dir,
    target_size = (img_height, img_width),
    batch_size = batch_size,
    class_mode = "categorical",
    shuffle = False)


# In[96]:

# Obtaining the prediction and storing it in "result", which is an array
 
result = model.predict_classes(val1_generator)


# In[97]:


# Converting the value(s) in the array to strings for easy viewing

for number in result:
    if number == 1:
        print("This image has the Golden Ratio!")
    else:
        print("This image doesn't have the Golden Ratio")

# Removing the image from the directory after the prediction
# This may not work on Windows systems and hence is commented

#import os
#os.remove(dst)

# Please ignore all warnings, the prediction(s) will be on the last (few) line(s)
# For more information, please refer to the .pptx file