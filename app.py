import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# whenever we load the image st gives a warning, this line of code will ignore that warning. for some reason im getting error so not running this line
# st.set_option('dreprecation.showfileUploaderEncoding', False)        

@st.cache(allow_output_mutation= True)                  # in case we make any changes and reload the model and run it again then it takes more time. So if there is cache then it will load quickly as it was already loaded previously


# Load the model .. 

def load_model(): 
  model= tf.keras.models.load_model('/content/my_model2.hdf5')         # give the path of the saved model. this function will load the model and return it
  return model
model= load_model()                        

# this is to give heading on the web
st.write("""
         # Drowsiness Detection System                                      
         """)  


file= st.file_uploader("Please upload the image of your eyes for detection", type=['jpg', 'png'])    # here the file will ask user to upload the image

# import libraries required 
import cv2
from PIL import Image, ImageOps                          # this is a python librarary which allows to do lot of computations on images
from tensorflow.keras.utils import load_img
import numpy as np
import tensorflow as tf

def import_and_predict(image_data, model):
  size= (224, 224)
  image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img = np.asarray(image)
  img = preprocess_input(img)
  img_reshape= img[np.newaxis, ...]                     # here we reshape it to 4 axis coz there are too many images trained 
  prediction= model.predict(img_reshape)

  return prediction 


if file is None: 
  st.text("Please upload an image file")
else: 
  image= Image.open(file)
  st.image(image, use_column_width= True)
  predictions= import_and_predict(image, model)
  class_names= ['Closed_Eyes', 'Open_Eyes'] 
  string= "This image most likely is: " +class_names[np.argmax(predictions)]
  st.success(string)



