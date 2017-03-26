import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic_raw_data.csv')
keep_cols = ['Age', 'Survived']
new_df = df1[keep_cols]

survived = new_df[new_df['Survived'] == 1]
dead = new_df[new_df['Survived'] == 0]

plt.xlabel('Age')
plt.ylabel('Survived')
plt.title('Age Survival Rates')

plt.hist(survived['Age'].dropna(), dead['Age'].dropna())


plt.show()




