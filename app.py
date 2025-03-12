import streamlit as st
import pandas as pd

# 🚀 Set page config at the very top (Fixes the error)
st.set_page_config(page_title="🏋️ Gym Equipment Tracker", layout="wide")

@st.cache_data
def load_data():
    xls = pd.ExcelFile("gym_data.xlsx")
    data_sheets = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    return data_sheets

data_sheets = load_data()

st.sidebar.title("🏋️ Gym Equipment Dashboard")
page = st.sidebar.radio("Choose a Category", list(data_sheets.keys()))

st.title(f"📋 {page} - Equipment List")
df = data_sheets[page]

# Convert Product Page URLs into Clickable Links
if "Product Page" in df.columns:
    df["Product Page"] = df["Product Page"].apply(lambda x: f'<a href="{x}" target="_blank">🔗 Click Here</a>' if x != "NA" else "NA")

# Convert Image URLs into Displayable Images, with a Sad Face for Stray Dog
if "Image URL" in df.columns:
    df["Image"] = df["Image URL"].apply(lambda x: 
    f'<img src="{x}" width="100">' if x != "NA" 
    else '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sad_Face_Emoji.png/240px-Sad_Face_Emoji.png" width="50">'
)




# Search and Filters
search_term = st.text_input("🔍 Search Equipment", "")
if search_term:
    df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

# Select Columns to Display
display_columns = ["Image", "Product Name", "Manufacturer", "Price", "Country", "Product Page"]
df_display = df[display_columns]

# Function to Convert DataFrame to HTML Table (For Clickable Links & Images)
def convert_df_to_html(df):
    return df.to_html(escape=False, index=False)

# Display Data in Clickable Format with Images
st.markdown(convert_df_to_html(df_display), unsafe_allow_html=True)

# Download Button
st.download_button("📥 Download Data", df.to_csv(index=False), f"{page.replace(' ', '_')}.csv", "text/csv")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by **Eduard Yegiazaryan**")
