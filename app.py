# to run using anaconda prompt: 
# cd C:\Users\Jake\OneDrive\Documents\VS Code\Streamlit\ACM Hackathon\
# streamlit run app.py

import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

stu = pd.read_csv("HackathonDataset.csv")
stu = stu.drop(columns="Unnamed: 0")

nonNumerical = ["First_Name","Last_Name","Education","Major","Date_Enrolled"]

st.title("Headstarter Student Analysis Dashboard")

st.header("Search for a student:")
customerID = st.number_input("Enter customer ID", step=1)
if customerID in stu["Customer_ID"].to_list():
    student = stu.loc[stu["Customer_ID"] == int(customerID)]
    st.dataframe(student)
else:
    st.text("No student found")


st.header("Sort students by metric:")
sortMetric = st.selectbox("Metric to sort by", stu.columns)
stu_sorted = stu.sort_values(by=sortMetric, ascending= False)
st.dataframe(stu_sorted)

# interact(bar_plotB, stat=list(stu.columns)[2:], direction = ['Ascending', 'Descending'])

x = st.selectbox("X Axis", stu.columns)
y1 = st.selectbox("Y Axis", stu.columns)

stu_sorted = stu.sort_values(by= y1, ascending= False)
fig1 = px.bar(stu_sorted, x=x, y=y1, width=800, height=600)
st.plotly_chart(fig1)


major = st.selectbox("Select major", stu["Major"].unique())
stu_major = stu.loc[stu['Major'] == major]
y2 = st.selectbox("Y2 Axis", stu.columns)

fig2 = px.bar(stu_major, x="Major", y=y2, width=800, height=600)
st.plotly_chart(fig2)


# low days since last cohort
# high minutes spent coding
# filter by grade
# high headstarter rating
# number of courses purchased
# 
metric = st.selectbox("Select metric", stu.columns.drop(nonNumerical))
st.write("Average: ", stu[metric].mean())
st.write("Number of students: ", len(stu))
st.write("Number in upper quartile: ", .25*len(stu))
boxplot = px.box(stu[metric])
st.plotly_chart(boxplot)

upperPercentReferred = st.slider("Upper percent for number of students referred: ", min_value=0, max_value=100)

stu_sorted = stu_sorted.sort_values(by= "Number_of_Students_Referred", ascending= False).head((round((upperPercentReferred * .01) * len(stu_sorted))))
#fig2 = px.bar(stu_sorted, x="Customer_ID", y=y2, width=800, height=600)


upperPercentDaysSinceCohort = st.slider("Upper percent for least number of days since last cohort: ", min_value=0, max_value=100)

stu_sorted = stu_sorted.sort_values(by= "Days_Since_Last_Cohort", ascending= True).head(round((upperPercentDaysSinceCohort * .01) * len(stu_sorted)))
length = len(stu_sorted.head(round((upperPercentDaysSinceCohort * .01) * len(stu_sorted))))
st.write("Number of students: ", length)
st.dataframe(stu_sorted.head(length))
#fig2 = px.bar(stu_sorted, x="Customer_ID", y=y2, width=800, height=600)


#Averages
st.write("Avg referrals: ", stu["Number_of_Students_Referred"].mean())
st.write("Avg courses purchased",stu["Num_Courses_Purchased"].mean())
st.write("Avg days since last Cohort",stu["Days_Since_Last_Cohort"].mean())
st.write("Avg amount spent on books",stu["Amount_Spent_on_Books"].mean())
st.write("Avg minutes spent on head starter",stu["Minutes_Spent_on_Headstarter"].mean())
st.write("Avg amount of questions completed",stu["Questions_Completed"].mean())
st.write("Avg amount of emails opened",stu["Email_Opens"].mean())
st.write("Avg amount of site visits",stu["Site_Visits_Per_Month"].mean())
st.write("Avg amount of avergae Team Rating",stu["Average_Teammate_Rating"].mean())
st.write("Avg amount of Cohorts Participated in",stu["Cohorts_Participated_In"].mean())
st.write("Avg amount for Highest leaderboard ranking",stu["Highest_Leaderboard_Rank"].mean())
st.write("Avg amount of Headstarter Rating",stu["Headstarter_Rating"].mean())
st.write("Avg amount of probability of offer",stu["Probability_Of_Getting_Offer"].mean())


x3 = st.selectbox("X3 Axis", stu.columns)
y3 = st.selectbox("Y3 Axis", stu.columns)

linechart = px.line(stu.sort_values(by= x3, ascending= False), x=x3, y=y3, title='Line Chart')
st.plotly_chart(linechart)


# MACHINE LEARNING MODEL
stu_ML = stu.drop(columns = nonNumerical)

stu_train = stu_ML.drop()



























