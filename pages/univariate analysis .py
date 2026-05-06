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
# add tabs 
tab1 , tab2 = st.tabs(['numerical','categorical'])
with tab1:
    st.header('Univariate Numerical')
    num_cols = df.select_dtypes(include='number').columns
    
    for col in num_cols:
        # إنشاء الرسمة الأول (Histogram)
        fig_hist = px.histogram(data_frame=df, x=col, title=f'Histogram of {col}')
        st.plotly_chart(fig_hist) # عرض الرسمة في ستريمليت
        
        # إنشاء الرسمة التانية (Box Plot)
        fig_box = px.box(data_frame=df, x=col, title=f'Box Plot of {col}')
        st.plotly_chart(fig_box) # عرض الرسمة في ستريمليت
        
        st.divider() 

with tab2:
    st.header('Univariate categorical')
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        # إنشاء الرسمة الأول (Histogram)
       # 1. إنشاء الرسمة
        fig_histo = px.histogram(
            data_frame=df, 
            x=col, 
            title=f'Histogram of {col}')
        
        # 2. ترتيب الأعمدة (للبيانات اللي فيها فئات أو Discrete Numbers)
        fig_histo.update_layout(xaxis={'categoryorder': 'total descending'})
        
        # 3. تعديل خصائص المحور (لو محتاج تعدل الـ Labels أو الشكل)
        fig_histo.update_xaxes(title_text=col)
    
    # 4. عرض الرسمة في ستريمليت
        st.plotly_chart(fig_histo)
        
        # إنشاء الرسمة التانية (Box Plot)
        fig_boxo = px.box(data_frame=df, x=col, title=f'Box Plot of {col}')
        st.plotly_chart(fig_boxo) # عرض الرسمة في ستريمليت
        
        st.divider() 
    
    
    