import streamlit as st
import pandas as pd

st.title('Students Performance in Exams Application')
st.markdown("""
This data set includes scores from three exams and a variety of personal, social, and economic factors that have interaction effects upon them.
* **Python libraries:** pandas, Altair, Matplotlib, Streamlit
* **Data source:** [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
""")




stdper=pd.read_csv('StudentsPerformance.csv')

st.sidebar.header('User Input Features')
unique_group = ['group A','group B','group C','group D','group E']
selected_group = st.sidebar.multiselect('race/ethnicity', unique_group, unique_group)
df_selected_group = stdper[(stdper['race/ethnicity'].isin(selected_group))]



st.header('Display ethnicity Selected')
st.write('Data Dimension: ' + str(df_selected_group.shape[0]) + ' rows and ' + str(df_selected_group.shape[1]) + ' columns.')
st.dataframe(df_selected_group)

st.markdown("""
### In page studper2:
- In scatter chart it shows the relationship between reading score and writing score which related to the level of education, when user change the level of education the reading and writing will change.
- In line chart it shows the relationship between reading score and writing score which related to the level of education, when user change the level of education the reading and writing will change.
- In bar chart, it shows the relationship between reading score and count of record related to level of education.
### In page studper3:
- In area chart it shows the relationship between math score and writing score related to the selection of race/ethnicity.
- In boxplot it shows the relationship between math score and writing score related to the selection of race/ethnicity, also it shows the max ,min,Q1,median,Q3 of math score.
### In page studper4:
- In donut chart it shows the relationship between writing score and level of education.
- In heatmap it shows the relationship between math score and race/ethnicity and writing score.
""")

