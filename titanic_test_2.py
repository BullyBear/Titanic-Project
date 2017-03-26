# import the relevant libraries

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import csv
import datetime
import pprint
import pdb

# read csv file into memory & sort columns by columns desired

df1 = pd.read_csv('titanic_raw_data.csv')

keep_cols = ["PassengerId", "Survived", "Pclass", "Sex", "Age"]

new_df = df1[keep_cols]

pprint.pprint(new_df)

# create a function for total # of survivors


def survivors():
	survivors = new_df["Survived"].sum()
	return survivors

survivors = survivors()
print("\tThe amount of people who survived were " + str(survivors) + " people.")


# create a function that compares survivors with Pclass


data_1 = pd.DataFrame(new_df, columns=[new_df['Survived']], index=['PassengerId'])
data_2 = pd.DataFrame(new_df, columns=[new_df['Pclass']], index=['PassengerId'])
data_3 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Pclass']], index=['PassengerId'])
data_4 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Sex']], index=['PassengerId'])
data_5 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Age']], index=['PassengerId'])

def survived(data_1):
	x = []
	count_x = 0
	for i in new_df["Survived"]:
		if i == 1:
			count_x += 1
			x.append(count_x)
	return count_x

def p_class(data_2):
	y = []
	count_y = 0
	for i in new_df["Pclass"]:
		if i == 1:
			count_y += 1
			y.append(count_y)
	return count_y

def combo(data_3):
	z = []
	count_z = 0	
	for i in range(len(new_df["Survived"])):
		if new_df["Survived"][i] == new_df["Pclass"][i]:
			count_z += 1
			z.append(count_z)
	return count_z


def combo_2(data_4):
	a = []
	count_a = 0
	for i in range(len(new_df["Survived"])):
		if new_df["Survived"][i] == new_df["Sex"][i]:
			count_a += 1
			a.append(count_a)
	return count_a


def combo_3(data_5):
	b = []
	count_b = 0
	for i in range(len(new_df["Survived"])):
		if new_df["Survived"][i] == new_df["Age"][i]:
			count_b += 1
			b.append(count_b)
	return count_b
	
count_x = survived(data_1)
count_y = p_class(data_2)
count_z = combo(data_3)
count_a = combo_2(data_4)
count_b = combo_3(data_5)

print(count_x, count_y, count_z, count_a, count_b)












