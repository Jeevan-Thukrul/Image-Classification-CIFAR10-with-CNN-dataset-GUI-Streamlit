import streamlit as st
from PIL import Image
import classify

st.set_option('deprecation.showfileUploaderEncoding', False)

st.markdown('<style>body{background-image: url("https://samyzaf.com/ML/cifar10/cifar1.jpg"); background-repeat: no-repeat; background-attachment: fixed; background-size: 100% 100%;} body::before{content: ""; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: rgba(1,1,1,0.80);}</style>',unsafe_allow_html=True)
st.markdown('<style>body{color: white; text-align: center;}</style>',unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

classes = {
        0: 'Airplane',
        1: 'Car',
        2: 'Bird',
        3: 'Cat',
        4: 'Deer',
        5: 'Dog',
        6: 'Frog',
        7: 'Horse',
        8: 'Ship',
        9: 'Truck'
      }

st.title("CIFAR 10 + CNN Classifier")
st.write("")
st.write("Train accuracy: 0.8148 \n\nTest accuracy: 0.7659")
st.write("")
st.subheader("By Jeevan Thukrul")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.write("Result...")
                st.write("")
                label = classify.predict(uploaded_file)
                label = label.item()
                res = classes.get(label)
                st.title(res)
