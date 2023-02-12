import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
st.write(df)

# gapmider GDP data Plot
year_options = df['year'].unique().tolist()
year = st.selectbox('Which year do you want to see?' , year_options, 0)
df = df[df['year']==year]

fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig.update_layout(width=800)
st.write(fig)

# COVID-19 data Plot
covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
#covid.columns = ['Country', 'Code', 'Date', 'Confirmed' 'Days since confirmed']
#covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
#country_options = covid['Country'].unique().tolist()
st.write(covid)

'''
date_options = covid['Date'].unique().tolist()
date = st.selectbox('Which date would you like to see?', date_options, 100)
country = st.selectbox('Which country would you like to see?', country_options, ['Brazil'])
                                                                                 
covid = covid[covid['Country'].isin(country)]
covid = covid[covid['Date']==date]

fig2 = px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000])
fig2.update_layout(width=800)
st.write(fig2)
'''
                                                                                

