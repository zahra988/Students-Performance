import streamlit as st
import pandas as pd
import altair as alt

stdper=pd.read_csv('StudentsPerformance.csv')
st.title('Students Performance in Exams')

level = st.select_slider("Select your level of education",stdper['parental level of education'].unique())
st.write(level)

plot_type=st.radio("select the plot type",['scatter','line','bar'])

if plot_type == 'scatter':
  pl = alt.Chart(stdper[stdper['parental level of education']==level]).mark_circle().encode(
    x = 'reading score',
    y ='writing score',
    size='writing score',
    tooltip = ['reading score','writing score'],
    color='reading score:N'
).interactive()

elif plot_type == 'line':
  pl = alt.Chart(stdper[stdper['parental level of education']==level]).mark_line().encode(
    x = 'reading score',
    y ='writing score',
    tooltip = ['reading score','writing score']
).interactive()

else:
 pl = alt.Chart(stdper[stdper['parental level of education']==level]).mark_bar(color='green').encode(
    x = 'reading score:N',
    y ='count()',
    tooltip = ['reading score','count()','parental level of education']
).interactive()
st.altair_chart(pl)

 

