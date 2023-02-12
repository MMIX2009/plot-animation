import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
st.write(df)

# gapmider GDP data Plot
year_options = df['year'].unique().tolist()
year = st.selectbox('Which year do you want to see?' , year_options, 0)
df = df[df['year']==year]

fig = px.scatter(df, x="gdpPrecap", y="LifeExp", size="pop", color="continent", hover_name="continent", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig.update_layout(width=800)
st.write(fig)
