import streamlit as st
import pandas as pd
import plotly.express as px

# DRC Cities population data Plot
st.header('DRC Cities Population data')
drc = pd.read_csv('drc_cities_pop.csv')
# st.write(drc.columns)
# Rename the columns
#covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
city_options = drc['City'].unique().tolist()
st.write(drc)

year_options = drc['Year'].unique().tolist()
year = st.selectbox('Which year would you like to see?', year_options)
city = st.multiselect('Which city would you like to see?', city_options, ['Kinshasa'])
                                                                                 
drc = drc[drc['City'].isin(city)]
# drc = drc[drc['Year']==year]
max_y = drc['Population'].max()
min_y = drc['Population'].min()

fig = px.bar(drc, x="City", y="Population", color="City", range_y=[min_y,max_y],
             animation_frame="Year", animation_group="City")

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
fig.update_layout(width=800)
st.write(fig)

max_yy = drc['Growth-Rate'].max()
min_yy = drc['Growth-Rate'].min()

fig2 = px.scatter(drc, x="Population", y="Growth-Rate", size="Population", color="City", hover_name="City", log_x=True, size_max=100, range_x=[min_y,max_y], range_y=[min_yy,max_yy],
                animation_frame="Year", animation_group="City")
fig2.update_layout(width=800)
st.write(fig2)
