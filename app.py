import streamlit as st
from PIL import Image

st.title(" Bienvenido a Sara,s Site")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image=Image.open("flores.jpg")
st.image(image, caption= "Interfaces Multimodales Sara")
                 

