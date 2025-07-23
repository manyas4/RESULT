import streamlit as st
import pandas as pd
import numpy
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.header(":red[🏆Result Dashboard]")
st.write("Select semester from below.")

df1 = pd.read_csv('sem1.csv')
df2 = pd.read_csv('sem2.csv')
df3 = pd.read_csv('sem3.csv')

p1 = (df1['Percentage'].sum()/6)
p2 = (df2['Percentage'].sum()/8)
p3 = (df3['Percentage'].sum()/9)



def show_sem1():
    fig1 = px.bar(df1, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 1',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig1.update_xaxes(showticklabels=False)
    st.plotly_chart(fig1)
    st.write(f'Percentage Semester 1 : {p1}')



def show_sem2():
    fig2 = px.bar(df2, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 2',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig2.update_xaxes(showticklabels=False)
    st.plotly_chart(fig2)
    st.write(f'Percentage Semester 2 : {p2}')


def show_sem3():
    fig3 = px.bar(df3, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 3',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig3.update_xaxes(showticklabels=False)
    st.plotly_chart(fig3)
    st.write(f'Percentage Semester 3 : {p3:.2f}')

options = ["Select an option", "Semester 1", "Semester 2", "Semester 3", "All"]
option = st.radio("Choose a semester to display result", options)

#option = st.radio('Select semester',['Semester 1','Semester 2','Semester 3','All'])

st.write(f'Selected option {option}.')

if option == 'Semester 1':
    show_sem1()

elif option == 'Semester 2':
    show_sem2()
    
elif option == 'Semester 3':
    show_sem3()


elif option == 'All':
    col1 , col2 , col3 = st.columns([33.33,33.33,33.33])

    with col1:
        show_sem1()
    with col2:
        show_sem2()
    with col3:
        show_sem3()
elif option == "Select an option":
 st.warning("Please select a option.")
    
#  FOR PREDICTION

data={
    'Sem':[1,2,3],
    'Percentage':[p1,p2,p3]
}

df4 = pd.DataFrame(data)
X = df4[['Sem']]
y = df4['Percentage']

model = LinearRegression()
model.fit(X,y)

predicted = model.predict([[4]])
st.write(f'Predicted percentage for Semester 4 : {predicted[0]:.2f}')


fig5 = px.bar(df4, x ='Sem' ,y='Percentage',color='Sem',title=' Semester Result ',
                  labels={'Sem':'Semester','Percentage':'Percentage'})
st.plotly_chart(fig5)



#no = st.number_input('Enter semester to predict percentage : ',min_value=4,max_value=8,step=1)
#predicted = model.predict([[no]])
#st.write(f'Predicted percentage for Semester {no}: {predicted[0]:.2f}')


