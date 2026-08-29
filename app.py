import streamlit as st  # Importa Streamlit para crear la aplicación.
st.markdown("<style>.stApp {background-color: #EAF2F8;} .titulo {background-color: #163A5F; color: white; padding: 18px; border-radius: 12px;} .resultado {background: linear-gradient(135deg,#FFFFFF,#DCEBFA); padding: 20px; border-radius: 12px; margin-top: 15px; transition: 0.3s;} .resultado:hover {transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15);} div.stButton > button {background-color: #1177CC; color: white; border: none; border-radius: 10px; padding: 10px 24px; font-weight: bold;}</style>", unsafe_allow_html=True)  # Reúne los estilos visuales desarrollados en los pasos anteriores.
st.markdown('<div class="titulo"><h1>Calculadora de Grado API</h1><p>Clasificación básica del petróleo</p></div>', unsafe_allow_html=True)  # Agrega título y descripción dentro de una tarjeta.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Solicita la gravedad específica del petróleo.
if st.button("Calcular"):  # Inicia el cálculo al presionar el botón.
    api = (141.5 / sg) - 131.5  # Calcula el grado API a partir de la gravedad específica.
    if api < 10:  # Comprueba si el grado API está por debajo de 10.
        tipo = "Muy pesado"  # Asigna la categoría muy pesado.
    elif api < 22.3:  # Comprueba si el valor está entre 10 y 22.3 °API.
        tipo = "Pesado"  # Asigna la categoría pesado.
    elif api < 31.1:  # Comprueba si el valor está entre 22.3 y 31.1 °API.
        tipo = "Medio"  # Asigna la categoría medio.
    else:  # Se ejecuta cuando el valor es igual o superior a 31.1 °API.
        tipo = "Liviano"  # Asigna la categoría liviano.
    st.markdown(f'<div class="resultado"><h2>{api:.2f} °API</h2><p><b>Clasificación:</b> {tipo}</p><p><b>SG ingresada:</b> {sg:.2f}</p></div>', unsafe_allow_html=True)  # Presenta grado API, clasificación y SG en una tarjeta final.
