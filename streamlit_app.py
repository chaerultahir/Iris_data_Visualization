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
