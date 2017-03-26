# import the relevant libraries

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import pprint
import pdb


# read csv file into memory & sort columns by columns desired

df1 = pd.read_csv('titanic_raw_data.csv')
keep_cols = ["PassengerId", "Survived", "Pclass", "Sex", "Age"]
new_df = df1[keep_cols]
pprint.pprint(new_df)


# compute statistical mean for survivability using heirarchical indexing

stats_df = new_df.groupby(['Pclass', 'Sex', 'Age'])[['Survived']].mean()
print(stats_df)


# find missing & incomplete data 

print(new_df.info())

# find mean age based on sex & pclass

missing_ages = new_df[new_df['Age'].isnull()]
mean_ages = new_df.groupby(['Pclass', 'Sex'])['Age'].mean()

def remove_na_ages(row):
	if pd.isnull(row['Age']):
		return mean_ages[row['Pclass'], row['Sex']]
	else:
		return row['Age']

new_df['Age'] = new_df.apply(remove_na_ages, axis=1)

print(new_df['Age'])


# create a function for total # of survivors

def survivors():
	survivors = new_df["Survived"].sum()
	return survivors

survivors = survivors()
print("\tThe amount of people who survived were " + str(survivors) + " people.")


# create a function that compares rate of survival with class


def p_class(new_df):
	grouped_by_p_class = new_df.groupby((['Pclass'])['Survived' == 1]).sum()
	return grouped_by_p_class


# create a function that compares rate of survival with sex

def sex(new_df):
	grouped_by_sex = new_df.groupby((['Sex'])['Survived' == 1]).sum()
	return grouped_by_sex



# create a function that compares rate of survival with age

def age(new_df):
	grouped_by_age_young = new_df.groupby([new_df['Age'] <= 3]).sum()['Survived'][1]
	grouped_by_age_middle = new_df.groupby([(new_df['Age'] >= 4) & (new_df['Age'] <= 10)]).sum()['Survived'][1]
	grouped_by_age_old = new_df.groupby([(new_df['Age'] >= 11) & (new_df['Age'] <= 17)]).sum()['Survived'][1]

	return (grouped_by_age_young, grouped_by_age_middle, grouped_by_age_old)


grouped_total_age = ['grouped_by_age_young', 'grouped_by_age_middle', 'grouped_by_age_old']

# call the functions & print

grouped_by_p_class = p_class(new_df)
grouped_by_sex = sex(new_df)
grouped_total_age = age(new_df)


print(grouped_by_p_class, grouped_by_sex, grouped_total_age)








