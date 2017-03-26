import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic_raw_data.csv')
keep_cols = ["PassengerId", "Survived", "Pclass", "Sex", "Age"]
new_df = df1[keep_cols]


first_class = new_df.groupby([new_df['Pclass'] == 1]).sum()['Survived'][1]
second_class= new_df.groupby([new_df['Pclass'] == 2]).sum()['Survived'][1]
third_class = new_df.groupby([new_df['Pclass'] == 3]).sum()['Survived'][1]

p_class = np.array([first_class, second_class, third_class])

plt.xlabel('PClass')
plt.ylabel('Survived')
plt.title('PClass Survival Rates', fontweight = 'bold')

labels = ['First Class', 'Second Class', 'Third Class']

plt.xticks(p_class, labels, rotation='vertical')

plt.ylim(0, 200)

plt.margins(0.2)

plt.subplots_adjust(bottom=0.15)

plt.plot(p_class, linestyle='', marker='o', color='blue')

plt.show()


