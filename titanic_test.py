import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import csv
import datetime
import pprint


df_data = pd.read_csv('titanic_raw_data.csv', sep=',', header=None)


pprint.pprint(df_data)
