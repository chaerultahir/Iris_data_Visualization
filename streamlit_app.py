import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris
from prediction import predict

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Iris Data Visualisation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to change the color of the sidebar
st.markdown(
    """
    <style>
    /* Mengubah warna sidebar */
    .css-1lcbmhc {
        background-color: #FFA500 !important; /* Oranye */
    }
    .css-18e3th9 {
        padding-top: 3rem !important;
    }
    .css-18ni7ap {
        padding: 1.5rem 1rem 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Menampilkan judul halaman utama
    st.title("Visualisasi Data Iris")


if __name__ == '__main__':
    main()




