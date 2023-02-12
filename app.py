import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
st.write(df)

# gapmider GDP data Plot
your_options = df['year'].unique().toList()
year = st.slectbox('Which year do you want to see?' , year_options, 0)
df = df[df['year']==year]

fig = px.scatter()
fig.update_layout(width=800)
st.write(fig)
