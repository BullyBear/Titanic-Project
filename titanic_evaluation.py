import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import csv
import datetime
import pprint

filepath = '/Users/WilliamStevens/Documents/titanic_project/titanic_raw_data.csv'

with open(filepath, 'r') as infile:
	content = infile.read()
	new_object = DataFrame(content, columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 
		'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], index=['one', 'two', 'three', 'four', 
		'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'])

pprint.pprint(new_object)






