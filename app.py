import pandas as pd
import numpy as np
import streamlit as st
import requests
import json
# from sklearn.neighbors import neighbors_class

import plotly.express as px



st.set_page_config(page_title="Eda page",
                   layout="centered",
                   initial_sidebar_state="auto"
                   )

st.title("Predictive Modeling")


# def file_selector(folder_path='.'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)

transform_options = ["Normal",
                         "Rescale",
                         "Standardization"]


classifier_list = [   "Decision Tree Classifier",                     
                       "K-Nearest Neighbors",
                       "Support Vector Classifier",
                       "CatBoost"]


# filename = file_selector()
# st.write('You selected `%s`' % filename)
selected_option="EDA"
if selected_option == "EDA":
    # eda_fun()
    st.write("Choose a transform type and model from the option below:")

    transform = st.selectbox("Select data transform",
                             transform_options)
    classifier = st.selectbox("Select classifier", classifier_list)

    # Crear un formulario con el método POST
    with st.form(key='my_form'):
        # Agregar un componente de carga de archivos
        
        uploaded_file = st.file_uploader("Selecciona un archivo")
        # Agregar un botón de envío
        
        submit_button = st.form_submit_button(label="Cargar archivo")


    # Si se ha cargado un archivo, enviar una solicitud POST al servidor
    if uploaded_file is not None:
           
        st.image(uploaded_file, caption='Imagen', width=400)
        reques_dat = {'transform': transform, 'classifier': classifier}
        url = "http://127.0.0.1:5000/upload"
        files = {"archivo": uploaded_file.getvalue()}
        response = requests.post(url, files=files,data=reques_dat)
        datos = response.json()
        st.title("Response Prediction:")
        st.markdown(f"<h3 style='text-align: center; color: red;'>Prediction : {datos['nomPredict']} </h3>", unsafe_allow_html=True)
        #st.write('Prediction:', datos['nomPredict'])

