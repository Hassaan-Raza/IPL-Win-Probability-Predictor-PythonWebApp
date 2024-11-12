import streamlit as st
import pickle
import pandas as pd

teams =['Royal Challengers Bangalore',
 'Kings XI Punjab',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Kochi Tuskers Kerala',
 'Pune Warriors',
 'Sunrisers Hyderabad',
 'Gujarat Lions',
 'Rising Pune Supergiants',
 'Rising Pune Supergiant',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

cities = ['Bangalore', 'Chandigarh', 'Mumbai', 'Kolkata', 'Jaipur',
       'Chennai', 'Hyderabad', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Cuttack',
       'Ahmedabad', 'Nagpur', 'Dharamsala', 'Kochi', 'Indore',
       'Visakhapatnam', 'Pune', 'Ranchi', 'Delhi', 'Abu Dhabi',
       'Rajkot', 'Kanpur', 'Bengaluru', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

pipe=pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win Predictor')

col1,col2= st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select the city',sorted(cities))

target= st.number_input('Enter the target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Enter the score')
with col4:
    overs = st.number_input('Enter the overs')
with col5:
    wickets = st.number_input('Enter the wickets')

if st.button("Predict Probability"):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10-wickets
    crr = score/overs
    rrr=(runs_left*6)/balls_left
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
                             'runs_left':[runs_left],'balls_left':[balls_left],'wickets_remaining':[wickets],
                             'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.header(batting_team + "-"+ str(round(win*100))+"%")
    st.header(bowling_team + "-"+ str(round(loss*100))+"%")