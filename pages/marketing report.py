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



# --- Sidebar (الفلاتر) ---
st.sidebar.header("لوحة التحكم بالبيانات")
selected_borough = st.sidebar.multiselect(
    "اختر المنطقة (Borough):",
    options=df['BOROUGH_NAME'].unique(),
    default=df['BOROUGH_NAME'].unique()
)

year_range = st.sidebar.slider(
    "اختر مدى السنوات:",
    min_value=int(df['sale_year'].min()),
    max_value=int(df['sale_year'].max()),
    value=(int(df['sale_year'].min()), int(df['sale_year'].max()))
)

# فلترة البيانات بناءً على الاختيارات
filtered_df = df[
    (df['BOROUGH_NAME'].isin(selected_borough)) & 
    (df['sale_year'].between(year_range[0], year_range[1]))
]

# --- Main Page (العرض الرئيسي) ---
st.title("🏙️ تقرير مبيعات العقارات في نيويورك")
st.markdown(f"يعرض البيانات لـ **{len(filtered_df)}** عملية بيع عقاري.")

# --- القسم الأول: مؤشرات الأداء الرئيسية (KPIs) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("إجمالي المبيعات", f"${filtered_df['SALE PRICE'].sum():,.0f}")
with col2:
    st.metric("متوسط سعر البيع", f"${filtered_df['SALE PRICE'].mean():,.0f}")
with col3:
    st.metric("إجمالي الوحدات", f"{filtered_df['TOTAL UNITS'].sum():,}")
with col4:
    st.metric("متوسط سنة البناء", int(filtered_df['YEAR BUILT'].mean()))

st.divider()

# --- القسم الثاني: الرسوم البيانية ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("توزيع المبيعات حسب المنطقة")
    fig_pie = px.pie(filtered_df, names='BOROUGH_NAME', values='SALE PRICE', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    st.subheader("تحليل السعر عبر الزمن")
    trend_data = filtered_df.groupby('sale_year')['SALE PRICE'].mean().reset_index()
    fig_line = px.line(trend_data, x='sale_year', y='SALE PRICE', markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

# --- القسم الثالث: تحليل الفئات والوحدات ---
st.subheader("أعلى 10 فئات مباني مبيعاً (Building Class Category)")
top_categories = filtered_df['BUILDING CLASS CATEGORY'].value_counts().nlargest(10).reset_index()
fig_bar = px.bar(top_categories, x='count', y='BUILDING CLASS CATEGORY', orientation='h', color='count')
st.plotly_chart(fig_bar, use_container_width=True)

# --- القسم الرابع: عرض البيانات الخام ---
with st.expander("🔍 عرض جدول البيانات التفصيلي"):
    st.write(filtered_df.head(100))