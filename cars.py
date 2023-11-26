import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
cars = pd.read_csv(link)
cars

cars['continent_fact'] = cars['continent'].factorize()[0]
cars['year'] = cars['year'].astype(str).replace(",",'')
cars['year'] = cars['year'].astype(int)
cars['continent'] = cars['continent'].replace(' Europe.','Europe').replace(' Japan.','Japan').replace(' US.','US')

st.title('Heatmat de corrélation')

fig1, ax1 = plt.subplots()
viz_correlation = sns.heatmap(cars.drop(columns='continent').corr(), center=0, cmap=sns.color_palette("vlag", as_cmap=True))
st.pyplot(fig1)

st.title('Création de boutons de filtrage par région')


filtred_data = {'Japan': cars[cars['continent']=='Japan'],'Europe': cars[cars['continent']=='Europe'],'US': cars[cars['continent']=='US']}
selected_continent = st.multiselect('selectionnez un continent', ['Japan','Europe','US'])
if not selected_continent:
    st.write('Aucune option sélectionnée')
else:
    st.write('Voici les valeurs sélectionnées : ',selected_continent)
filtred_dataset = pd.concat(filtred_data[continent]for continent in selected_continent)

fig3, ax3 = plt.subplots()
dist24 = sns.kdeplot(data= filtred_dataset, x="hp", hue="continent", multiple="stack")
st.pyplot(fig3)


st.title('Nombre de voitures par année')

fig4, ax4 = plt.subplots()
d = sns.countplot(filtred_dataset, x = 'year')

st.pyplot(fig4)

st.title('Mpg par région')

fig5, ax5 = plt.subplots()
d2 = sns.boxplot(filtred_dataset, x = 'continent', y = 'mpg')

st.pyplot(fig5)


st.title('Le poids par région')

fig6, ax6 = plt.subplots()
d3 = sns.kdeplot(filtred_dataset, x="weightlbs", hue="continent", multiple="stack")
st.pyplot(fig6)


st.title('La puissance par nombre de cylindres avec distinction par région')

fig7, ax7 = plt.subplots()
d2 = sns.boxplot(filtred_dataset, x = 'cylinders', y = 'hp', hue= 'continent')
st.pyplot(fig7)