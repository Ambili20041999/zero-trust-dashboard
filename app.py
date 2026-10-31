import streamlit as st
import pandas as pd
import database
from login import *
from trust_engine import *

st.set_page_config(
    page_title="Zero Trust Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Create database
database.create_database()

# Login
if not check_login():
    login()
    st.stop()

# Sidebar
st.sidebar.title("Zero Trust Dashboard")

st.title("Zero Trust Dashboard for IoT Networks")

st.subheader("Add New IoT Device")

device_id = st.text_input("Device ID")

capability = st.number_input(
    "Capability",
    min_value=0,
    max_value=100,
    value=50
)

feature = st.number_input(
    "Feature",
    min_value=0,
    max_value=100,
    value=50
)

activity = st.number_input(
    "Activity",
    min_value=0,
    max_value=100,
    value=50
)

if st.button("Add Device"):

    if device_id == "":
        st.error("Please Enter Device ID")

    else:

        trust_score = calculate_trust(
            capability,
            feature,
            activity
        )

        status = classify_device(trust_score)

        database.insert_device(
            device_id,
            capability,
            feature,
            activity,
            trust_score,
            status
        )

        st.success("Device Added Successfully")

        st.write("### Result")
        st.write("Trust Score :", trust_score)
        st.write("Status :", status)

# ------------------------
# Device List
# ------------------------

st.subheader("Device List")

rows = database.get_all_devices()

if len(rows) > 0:

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Device ID",
            "Capability",
            "Feature",
            "Activity",
            "Trust Score",
            "Status"
        ]
    )

    st.dataframe(df, use_container_width=True)

else:

    st.warning("No Devices Found")