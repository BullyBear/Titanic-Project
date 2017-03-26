import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic_raw_data.csv')
keep_cols = ['Age', 'Survived']
new_df = df1[keep_cols]

survived = new_df[new_df['Survived'] == 1]
dead = new_df[new_df['Survived'] == 0]

def hist(column_data, xlabel):
	plt.xlabel(xlabel)
	plt.ylabel('Frequency')
	plt.title('Age Survival Rates Amongst the Living & Dead')
	plt.hist(column_data)
	plt.show()

hist(survived['Age'].dropna(), 'Age Distribution of Passengers Who Survived')
hist(dead['Age'].dropna(), 'Age Distributions of Passengers Who Died')




