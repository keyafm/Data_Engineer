import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# Configurar título y cargar imagen
st.title("Aplicación de localización de estaciones de carga de coches eléctricos en Madrid")
st.image("ruta_de_la_imagen.png", caption="Imagen de estaciones de carga", use_column_width=True)

# Descripción con expander
with st.beta_expander("Ver descripción"):
    st.write("Aquí puedes escribir una descripción más detallada de la aplicación.")

# Leer los datos
data = pd.read_csv("Ejercicio/red_recarga_acceso_publico_2021.csv")
st.write("Código para imprimir los datos:")
st.echo()
st.dataframe(data)

# Mostrar mapa con estaciones
st.map(data)

# Mostrar gráfico de barras por distrito
st.bar_chart(data["Distrito"].value_counts())

# Mostrar gráfico de barras por operador
st.bar_chart(data["Operador"].value_counts())

# Selección de página
page = st.sidebar.selectbox("Selecciona una página", ["Inicio", "Datos"])

# Mostrar la página correspondiente según la selección del usuario
if page == "Inicio":
    # Página de inicio
    st.write("Bienvenido a la página de inicio")
else:
    # Página de datos
    st.write("Bienvenido a la página de datos")
