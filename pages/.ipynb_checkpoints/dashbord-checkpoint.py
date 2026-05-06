import streamlit as st
import pandas as pd 
import plotly.express as px
st.set_page_config(layout='wide', page_title='NYC', page_icon='🍎')
# add title 
st.header('NYC property prices')
st.image("https://www.kayak.com/rimg/dimg/dynamic/376-1686302711-nyc_introduction_hero1_gettyimages-1152797059-scaled.jpeg?height=768&width=1366&crop=true")
df=pd.read_csv("cleaned_df.csv")
st.header("Data Overview")
st.dataframe(df.head(5), use_container_width=True)
st.title("Dashboard KBIs")
import streamlit as st

# حساب القيم
total_sales = df['SALE PRICE'].sum()
avg_price = df['SALE PRICE'].mean()
total_units = df['TOTAL UNITS'].sum()

# حساب السعر لكل قدم مربع (تأكد من التعامل مع القيم الصفرية في المساحة)
# Price per SqFt = Total Sales / Total Gross Square Feet
price_per_sqft = df['SALE PRICE'].sum() / df['GROSS SQUARE FEET'].replace(0, 1).sum()


st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

col1.metric("إجمالي المبيعات", f"${total_sales:,.0f}")
col2.metric("متوسط السعر", f"${avg_price:,.0f}")
col3.metric("إجمالي الوحدات المباعة", f"{total_units:,}")
col4.metric("سعر القدم المربع", f"${price_per_sqft:,.2f}")

import streamlit as st
import plotly.express as px

# Setup Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Time Trends", "📍 Location", "🏠 Property Types", "💰 Financials"])

with tab1:
    st.header("Sales Trends Over Time")
    # Example: Monthly trend
    monthly_sales = df.groupby('sale_month')['SALE PRICE'].sum().reset_index()
    fig = px.line(monthly_sales, x='sale_month', y='SALE PRICE', markers=True)
    st.plotly_chart(fig)

with tab2:
    st.header("Borough Performance")
    # Example: Bar chart of sales by Borough
    borough_sales = df['BOROUGH_NAME'].value_counts()
    st.bar_chart(borough_sales)

with tab3:
    st.header("Building Categories")
    # Example: Pie chart
    fig_pie = px.pie(df, names='BUILDING CLASS CATEGORY', title='Market Share by Property Type')
    st.plotly_chart(fig_pie)

with tab4:
    st.header("Price vs. Size Analysis")
    # Example: Scatter plot
    fig_scatter = px.scatter(df[df['SALE PRICE'] > 10000], 
                             x='GROSS SQUARE FEET', 
                             y='SALE PRICE', 
                             color='BOROUGH_NAME',
                             hover_data=['NEIGHBORHOOD'])
    st.plotly_chart(fig_scatter)

