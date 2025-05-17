import pandas as pd
import streamlit as st
import plotly.express as px

# Set the title for the app
st.title('Data Visualization with Streamlit')
st.write('This app allows you to insert data, filter it, and visualize it interactively.')

# --- Initialize Session State Data ---
# Initialize the data if not already present in session_state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Name', 'Age', 'City'])

# --- Sidebar for Input ---
st.sidebar.header('Data Insertion')
st.sidebar.write('Add new rows of data')

# Input fields in the sidebar for the user to input new data
name = st.sidebar.text_input('Name')
age = st.sidebar.number_input('Age', min_value=0)
city = st.sidebar.text_input('City')

# Button to add the data into the DataFrame
if st.sidebar.button('Add Data'):
    # Append the new data to the DataFrame in session_state
    new_data = pd.DataFrame({'Name': [name], 'Age': [age], 'City': [city]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.sidebar.write('Data Added!')

# Show the current data in the app
st.subheader('Current Data')
st.write(st.session_state.data)

# --- Sidebar for Filtering ---
st.sidebar.header('Filter Data')
filter_city = st.sidebar.selectbox('Select City', st.session_state.data['City'].unique())
filtered_data = st.session_state.data[st.session_state.data['City'] == filter_city]

st.sidebar.write(f"Showing data for {filter_city}")
st.write(filtered_data)

# --- Visualization ---
# Display bar chart for age distribution
st.subheader('Age Distribution by City')
fig = px.bar(filtered_data, x='Name', y='Age', color='City', title="Age Distribution by City")
st.plotly_chart(fig)

# --- Deploying Your Streamlit App ---
st.write("""
    ### How to Deploy Your Streamlit App
    1. Save this code to a Python file, e.g., `app.py`.
    2. To run the app locally, open a terminal and run:
        ```bash
        streamlit run app.py
        ```
    3. To deploy the app online, create an account on Streamlit Cloud (https://share.streamlit.io) and upload the code.
    4. Follow the instructions provided to deploy the app to Streamlit Cloud.
""")


selected_Year = st.sidebar.selectbox("Select Year",['All'] + list(books_df))