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


# create a function for total # of survivors

def survivors():
	survivors = new_df["Survived"].sum()
	return survivors

survivors = survivors()
print("\tThe amount of people who survived were " + str(survivors) + " people.")


# munge the csv file into 3 seperate dataframes to be used as function inputs for later on

data_1 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Pclass']], index=['PassengerId'])
data_2 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Sex']], index=['PassengerId'])
data_3 = pd.DataFrame(new_df, columns=[new_df['Survived'], new_df['Age']], index=['PassengerId'])


# create a function that compares rate of survival with class

def p_class(data_1):
	class_1 = []
	class_2 = []
	class_3 = []
	count_first_class = 0	
	count_second_class = 0
	count_third_class = 0

	for i in range(len(new_df["Survived"])):

		if new_df["Survived"][i] == new_df["Pclass"][i]:
			count_first_class += 1
			class_1.append(count_first_class)

		if (new_df["Survived"][i] == 1) & (new_df["Pclass"][i] == 2):
			count_second_class += 1
			class_2.append(count_second_class)

		if (new_df["Survived"][i] == 1) & (new_df["Pclass"][i] == 3):
			count_third_class += 1
			class_3.append(count_third_class)

	return (count_first_class, count_second_class, count_third_class)
	

# create a function that compares rate of survival with sex

def sex(data_2):
	class_male = []
	class_female = []
	count_male = 0
	count_female = 0

	for i in range(len(new_df["Survived"])):

		if (new_df["Survived"][i] == 1) & (new_df["Sex"][i] == 'male'):
			count_male += 1
			class_male.append(count_male)

		if (new_df["Survived"][i] == 1) & (new_df["Sex"][i] == 'female'):
			count_female += 1
			class_female.append(count_female)
	
	return (count_male, count_female)


# create a function that compares rate or survival with age

def age(data_3):
	class_three_and_under = []
	class_four_to_ten = []
	class_eleven_to_seventeen = []
	count_three_and_under = 0
	count_four_to_ten = 0
	count_eleven_to_seventeen = 0

	for i in range(len(new_df["Survived"])):

		if (new_df["Survived"][i] == 1) & (new_df["Age"][i] <= 3):
			count_three_and_under += 1
			class_three_and_under.append(count_three_and_under)

		if (new_df["Survived"][i] == 1) & (new_df["Age"][i] >= 4) & (new_df["Age"][i] <= 10):
			count_four_to_ten += 1
			class_four_to_ten.append(count_four_to_ten) 

		if (new_df["Survived"][i] == 1) & (new_df["Age"][i] >= 11) & (new_df["Age"][i] <= 17):
			count_eleven_to_seventeen += 1
			class_eleven_to_seventeen.append(count_eleven_to_seventeen)

	return (count_three_and_under, count_four_to_ten, count_eleven_to_seventeen)


# consolidate each function's return statements
	
p_total = ['count_first_class', 'count_second_class', 'count_third_class']
sex_total = ['count_male', 'count_female']
age_total = ['count_three_and_under', 'count_four_to_ten', 'count_eleven_to_seventeen']


# call the functions & print

p_total = p_class(data_1)
sex_total = sex(data_2)
age_total = age(data_3)


print(p_total, sex_total, age_total)




