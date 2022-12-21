import streamlit as st
import pandas as pd
import altair as alt

stdper=pd.read_csv('StudentsPerformance.csv')
st.title('Students Performance in Exams')
group = st.selectbox("Select your race/ethnicity",stdper['race/ethnicity'].unique())
st.write(group)
chart_type=st.radio('select chart type',['area','boxplot'])

if chart_type == 'area':
  ch = alt.Chart(stdper[stdper['race/ethnicity']==group]).mark_area(color='yellow').encode(
    x = 'math score',
    y ='writing score',
    tooltip = ['math score','writing score']
).interactive()

else:
  ch= alt.Chart(stdper[stdper['race/ethnicity']==group]).mark_boxplot(extent='min-max').encode(
    x='math score:O',
    y='writing score:Q'
).interactive()
st.altair_chart(ch)


 

