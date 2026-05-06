import streamlit as st
import pandas as pd 
st.set_page_config(layout='wide', page_title='NYC', page_icon='🍎')
# add title 
st.header('NYC property prices')
st.image("https://www.kayak.com/rimg/dimg/dynamic/376-1686302711-nyc_introduction_hero1_gettyimages-1152797059-scaled.jpeg?height=768&width=1366&crop=true")
df=pd.read_csv("cleaned_df.csv")
st.header("Data Overview")
st.dataframe(df.head(5), use_container_width=True)
# data description 
st.header("Data Description")


# 1. Define your columns and their descriptions
data_description = {
    "Column Name": [
        "BOROUGH", "NEIGHBORHOOD", "BUILDING CLASS CATEGORY", "TAX CLASS AT PRESENT",
        "BLOCK", "LOT", "BUILDING CLASS AT PRESENT", "ZIP CODE", "RESIDENTIAL UNITS",
        "COMMERCIAL UNITS", "TOTAL UNITS", "LAND SQUARE FEET", "GROSS SQUARE FEET",
        "YEAR BUILT", "TAX CLASS AT TIME OF SALE", "BUILDING CLASS AT TIME OF SALE",
        "SALE PRICE", "SALE DATE", "sale_year", "sale_month", "BOROUGH_NAME"
    ],
    "Description": [
        "The borough code where the property is located.",
        "The name of the neighborhood.",
        "Category of the building (e.g., Residential, Commercial).",
        "The tax class at the time of the data export.",
        "The tax block where the property is located.",
        "The tax lot where the property is located.",
        "The building class at the time of data export.",
        "The property's zip code.",
        "Number of residential units in the building.",
        "Number of commercial units in the building.",
        "Total number of units (Residential + Commercial).",
        "The land area of the property in square feet.",
        "The total building area in square feet.",
        "The year the building was constructed.",
        "The tax class at the time the property was sold.",
        "The building class at the time the property was sold.",
        "The price paid for the property.",
        "The date the property was sold.",
        "The year extracted from the sale date.",
        "The month extracted from the sale date.",
        "The full name of the Borough (e.g., Manhattan, Brooklyn)."
    ]
}

# 2. Convert to DataFrame
description_df = pd.DataFrame(data_description)

# 3. Streamlit Display
st.title("Data Dictionary")
st.markdown("Overview of the features in the New York City Real Estate Sales dataset.")

# Use st.table for a static, easy-to-read list
st.table(description_df)