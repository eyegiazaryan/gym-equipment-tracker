import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    xls = pd.ExcelFile("gym_data.xlsx")
    data_sheets = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    return data_sheets


st.set_page_config(page_title="🏋️ Gym Equipment Tracker", layout="wide")

data_sheets = load_data()


st.sidebar.title("🏋️ Gym Equipment Dashboard")
page = st.sidebar.radio("Choose a Category", list(data_sheets.keys()))

st.title(f"📋 {page} - Equipment List")
df = data_sheets[page]


if "Product Page" in df.columns:
    df["Product Page"] = df["Product Page"].apply(lambda x: f'<a href="{x}" target="_blank">🔗 Click Here</a>' if x != "NA" else "NA")

if "Image URL" in df.columns:
    df["Image"] = df["Image URL"].apply(lambda x: f'<img src="{x}" width="100">' if x != "NA" else "No Image")


search_term = st.text_input("🔍 Search Equipment", "")
if search_term:
    df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]


display_columns = ["Image", "Product Name", "Manufacturer", "Price", "Country", "Product Page"]
df_display = df[display_columns]

def convert_df_to_html(df):
    return df.to_html(escape=False, index=False)


st.markdown(convert_df_to_html(df_display), unsafe_allow_html=True)


st.download_button("📥 Download Data", df.to_csv(index=False), f"{page.replace(' ', '_')}.csv", "text/csv")

st.sidebar.markdown("---")
st.sidebar.write("Developed by Your Name 🚀")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by **Eduard Yegiazaryan**")
