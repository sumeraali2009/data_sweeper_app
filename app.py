import streamlit as st
import pandas as pd

# Configure Streamlit theme
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f0f0;
    }
    .sidebar-content {
        background: #f0f0f0;
    }
    .main {
        background: #f0f0f0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and header
st.title("Data Cleaner App")
st.write("Clean and visualize your CSV, XLS, and XLSX files")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xls', 'xlsx', 'text/plain'])

# Check if file is uploaded
if uploaded_file is not None:
    # Display file details
    st.write("File Details:")
    st.write("File Name:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)
    st.write("File Size:", uploaded_file.size)

    # Read file into DataFrame
    if uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.type == 'text/plain':
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.type == 'application/vnd.ms-excel':
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(uploaded_file)

    # Display DataFrame
    st.write("Data Preview:")
    st.write(df)

    # Data cleaning options
    st.write("Data Cleaning Options:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Remove Rows with Missing Values", help="Remove rows with missing values"):
            df.dropna(inplace=True)
            st.write("Data after removing missing values:")
            st.write(df)
    with col2:
        if st.button("Remove Duplicates", help="Remove duplicate rows"):
            df.drop_duplicates(inplace=True)
            st.write("Data after removing duplicates:")
            st.write(df)
    with col3:
        if st.button("Remove Columns", help="Remove selected columns"):
            cols = df.columns.tolist()
            cols_to_remove = st.multiselect("Select columns to remove", cols)
            df.drop(cols_to_remove, axis=1, inplace=True)
            st.write("Data after removing columns:")
            st.write(df)

    # Download cleaned data
    st.write("Download Cleaned Data:")
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False)
    csv = convert_df(df)
    b64 = csv.encode('utf-8').decode()
    st.markdown(f'<a href="data:text/csv;base64,{b64}" download="{uploaded_file.name}.csv" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Download CSV File</a>', unsafe_allow_html=True)
