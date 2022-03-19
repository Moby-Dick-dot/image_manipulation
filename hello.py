import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
file = st.file_uploader('Upload An Image')
if file:  # if user uploaded file
    img = Image.open(file)

st.title("Here is the image you've selected")
resized_image = img.resize((336, 336))
st.image(resized_image)