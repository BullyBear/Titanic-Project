import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic_raw_data.csv')
keep_cols = ["PassengerId", "Survived", "Pclass", "Sex", "Age"]
new_df = df1[keep_cols]


men = new_df.groupby([new_df['Sex'] == 'male']).sum()['Survived'][1]
women = new_df.groupby([new_df['Sex'] == 'female']).sum()['Survived'][1]

gender = np.array([men, women])

plt.xlabel('Gender')
plt.ylabel('Survived')
plt.title('Gender Survival Rates', fontweight='bold')

labels = ['Male', 'Female']

plt.xticks(gender, labels, rotation='vertical')

plt.ylim(0, 3)

plt.margins(0.2)

plt.subplots_adjust(bottom=0.15)

plt.bar(men, height=1, width=10, color='red')
plt.bar(women, height=2.125, width=10, color='red')

plt.show()



