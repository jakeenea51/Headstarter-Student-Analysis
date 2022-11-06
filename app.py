# IMPORTS
import pandas as pd
import plotly.express as px
import streamlit as st

# READ CSV INTO DATAFRAME
stu = pd.read_csv("HackathonDataset.csv")
stu = stu.drop(columns="Unnamed: 0")

# List of non numerical fields
nonNumerical = ["First_Name","Last_Name","Education","Major","Date_Enrolled"]

# Page config
st.set_page_config(page_title="Headstarter Student Analysis Dashboard", page_icon="📚", layout="centered")
st.title("Headstarter Student Analysis Dashboard")


# STUDENT SEARCH
st.header("Search for a student:")
customerID = st.number_input("Enter customer ID", step=1)
if customerID in stu["Customer_ID"].to_list():
    student = stu.loc[stu["Customer_ID"] == int(customerID)]
    st.dataframe(student)
else:
    st.text("No student found")


# STUDENT SORT
st.header("Sort students by metric:")
sortMetric = st.selectbox("Metric to sort by", stu.columns)
ascending = st.checkbox("Ascending")
stu_sorted = stu.sort_values(by=sortMetric, ascending= ascending)
st.dataframe(stu_sorted)


# BOX PLOTS
st.header("Display box plots for metrics:")
metric = st.selectbox("Select metric", stu.columns.drop(nonNumerical))
st.write("Average: ", round(stu[metric].mean(), 2))
boxplot = px.box(stu[metric])
st.plotly_chart(boxplot)


# ANALYSIS OF HIGH CORRELATIONS
st.header("Analysis of high correlations:")
st.write("Questions completed vs. Prob. of Getting an Offer")
scatterplot = px.scatter(stu, x=stu["Questions_Completed"], y=stu["Probability_Of_Getting_Offer"], trendline="ols")
st.plotly_chart(scatterplot)

st.write("Minutes spent coding vs. Amount spent on courses")
scatterplot = px.scatter(stu, x=stu["Minutes_Spent_Coding"], y=stu["Amount_Spent_On_Courses"], trendline="ols")
st.plotly_chart(scatterplot)


# FINE-TUNE SELECT STUDENTS BASED ON IMPORTANT METRICS
# Metrics we valued:
#   - low days since last cohort
#   - high minutes spent coding
#   - filter by grade
#   - high headstarter rating
#   - number of courses purchased
st.header("Fine-tune select students based on rankings in important metrics:")
upperPercentReferred = st.slider("Top % of number of students referred: ", value=100, min_value=0, max_value=100)
stu_sorted = stu_sorted.sort_values(by= "Number_of_Students_Referred", ascending= False).head((round((upperPercentReferred * .01) * len(stu_sorted))))

upperMinsCoding = st.slider("Top % of minutes spent coding: ", value=100, min_value=0, max_value=100)
stu_sorted = stu_sorted.sort_values(by= "Minutes_Spent_Coding", ascending= False).head((round((upperMinsCoding * .01) * len(stu_sorted))))

upperHeadstarterRating = st.slider("Top % of headstarter rating: ", value=100, min_value=0, max_value=100)
stu_sorted = stu_sorted.sort_values(by= "Headstarter_Rating", ascending= False).head((round((upperHeadstarterRating * .01) * len(stu_sorted))))

upperQuestionsCompleted = st.slider("Top % of questions completed: ", value=100, min_value=0, max_value=100)
stu_sorted = stu_sorted.sort_values(by= "Questions_Completed", ascending= False).head((round((upperQuestionsCompleted * .01) * len(stu_sorted))))

upperEmailsOpened = st.slider("Top % of emails opened: ", value=100, min_value=0, max_value=100)
stu_sorted = stu_sorted.sort_values(by= "Email_Opens", ascending= False).head((round((upperEmailsOpened * .01) * len(stu_sorted))))

upperPercentDaysSinceCohort = st.slider("Top % of least days since last being part of a cohort: ", value=100, min_value=0, max_value=100)

# Display dataframe of students that meet the above criteria
stu_sorted = stu_sorted.sort_values(by= "Days_Since_Last_Cohort", ascending= True).head(round((upperPercentDaysSinceCohort * .01) * len(stu_sorted)))
length = len(stu_sorted.head(round((upperPercentDaysSinceCohort * .01) * len(stu_sorted))))
st.write("Number of students: ", length)
st.dataframe(stu_sorted.head(length))
