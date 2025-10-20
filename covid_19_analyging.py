import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("D:\\INTERN\\data analisys\\covid_19_india.csv")

#-----------------Cleaning data ----------------

data.drop_duplicates(inplace=True)
data.drop(data[(data==0).any(axis=1)].index,inplace=True)

#-----------------info of maniplated data---------------------

print("Information\n",data.info())

#-----------------average----------------------------

print('\naverage of Confirmed:',data['Confirmed'].mean().round(2))
print('average of cured:',data['Cured'].mean().round(2))
print('\naverage of Deaths:',data['Deaths'].mean().round(2))

#-------------------visualization--------------------------

top_states = data.groupby("State/UnionTerritory")["Confirmed"].max().sort_values(ascending=False).head(10).reset_index()
print(top_states)

#Bar graph

plt.figure(figsize=(10,5))
plt.title('Top 10 States of confirmed cases')
plt.xlabel('States')
plt.ylabel('Confirmed cases')
plt.xticks(rotation=50)
plt.bar(top_states['State/UnionTerritory'],top_states['Confirmed'])
plt.show()

#Scatter plot

plt.figure(figsize=(8,6))
plt.scatter(data["Confirmed"], data["Deaths"], alpha=0.6, color="green")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.title(" Confirmed vs Deaths")
plt.show()

# Heatmap

ndata = data[["Confirmed", "Cured", "Deaths"]]
corr = ndata.corr()

plt.figure(figsize=(6,5))
plt.matshow(corr, cmap="RdBu", fignum=1)
plt.colorbar(label="Correlation")

ticks = np.arange(len(corr.columns))
plt.xticks(ticks, corr.columns, rotation=45)
plt.yticks(ticks, corr.columns)

plt.title("Correlation Heatmap of COVID-19 Data", pad=20)
plt.show()
