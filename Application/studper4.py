import streamlit as st
import pandas as pd
import altair as alt

stdper=pd.read_csv('StudentsPerformance.csv')
st.title('Students Performance in Exams')

plot_type=st.radio("select the plot type",['donut','Heatmap'])

if plot_type == 'donut':
  pl = alt.Chart(stdper).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field='writing score', type="quantitative"),
    color=alt.Color(field="parental level of education", type="nominal"),
     tooltip = ['writing score','parental level of education']
).interactive()

else:
  pl = alt.Chart(stdper).mark_rect().encode(
    x='math score:O',
    y='race/ethnicity:O',
    color=alt.Color('writing score:Q', scale=alt.Scale(scheme="inferno")),
    tooltip=['math score','writing score','race/ethnicity']
).interactive()
st.altair_chart(pl)

st.button('re-run')


