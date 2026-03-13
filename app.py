import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

model = load_model("VGG16_best.h5")

class_names = [
 'animal fish',
 'animal fish bass',
 'fish sea_food black_sea_sprat',
 'fish sea_food gilt_head_bream',
 'fish sea_food hourse_mackerel',
 'fish sea_food red_mullet',
 'fish sea_food red_sea_bream',
 'fish sea_food sea_bass',
 'fish sea_food shrimp',
 'fish sea_food striped_red_mullet',
 'fish sea_food trout'
]

st.title("🐟 Fish Image Classifier")

uploaded_file = st.file_uploader("Upload fish image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((224,224))

    st.image(img, caption="Uploaded Image", width=300)

    img_array = image.img_to_array(img)

    # ✅ NORMALIZE
    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)

    predicted_index = np.argmax(predictions)

    predicted_class = class_names[predicted_index]

    confidence = np.max(predictions) * 100

    # st.write("Prediction probabilities:", predictions)

    st.success(f"Predicted Fish: **{predicted_class}**")
    st.info(f"Confidence: **{confidence:.2f}%**")