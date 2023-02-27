import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import os
import time

st.set_page_config(page_title="Real-Time Data Science Dashboard", page_icon="✅", layout="wide",)

st.title("Data Science Dashboard - Bank Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "professionelles-marketing.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "bank-full.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

# top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["job"] == job_filter]

df["age_new"] = df["age"] * np.random.choice(range(1, 5))
df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

# creating KPIs
avg_age = np.mean(df["age_new"])

count_married = int(df[(df["marital"] == "married")]["marital"].count() + np.random.choice(range(1, 30)))

balance = np.mean(df["balance_new"])

with placeholder.container():

     # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Age ⏳",
            value=round(avg_age),
            delta=round(avg_age) - 10,
        )
        
        kpi2.metric(
            label="Married Count 💍",
            value=int(count_married),
            delta=-10 + count_married,
        )
        
        kpi3.metric(
            label="A/C Balance ＄",
            value=f"$ {round(balance,2)} ",
            delta=-round(balance / count_married) * 100,
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)

st.write("**Thank you for reading, and Happy Streamlit-ing!:balloon:**") 