import streamlit as st
from PIL import Image

st.title(" Bienvenido a Sara,s Site")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image=Image.open("flores.jpg")
st.image(image, caption= "Interfaces Multimodales Sara")

texto=st.text_input("Escribe algo", "Este es mi texto")
st.write("el texto escrito es", texto)

st.subheader("Ahora Usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto") 
with col2:
  st.subheader("Esta es la segunda")
  modo=st.radio("Que modalidad es la principal de tu interfaz",("Visual", "auditivo", "tactil"))
  if modo=="Visual":
    st.write("lA VISTA ES FUNDAMENTAL PARA TU INTERFAZ")
  if modo=="auditivo":
    st.write("skjasjdklas")
  if modo=="tactil":
    st.write("jdasdlaksdadoj")



st.subheader("uso de botones")
             



  

                 

