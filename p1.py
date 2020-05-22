# Import libraries necessary for this project
import numpy as np
import pandas as pd
from time import time
# from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualization code visuals.py
# import visuals as vs

# Pretty display for notebooks
# %matplotlib inline

# Load the Census dataset
data = pd.read_csv("census.csv")

# Success - Display the first record
# display(data.head(n=10))
# TODO: Total number of records
n_records = np.size(data,0)

# TODO: Number of records where individual's income is more than $50,000
n_greater_50k = np.count_nonzero(data['income'] == '>50K')

# TODO: Number of records where individual's income is at most $50,000
n_at_most_50k = np.count_nonzero(data['income'] == '<=50K')

# TODO: Percentage of individuals whose income is more than $50,000
greater_percent = (n_greater_50k/n_records)*100

# Print the results
print("Total number of records: {}".format(n_records))
print("Individuals making more than $50,000: {}".format(n_greater_50k))
print("Individuals making at most $50,000: {}".format(n_at_most_50k))
print("Percentage of individuals making more than $50,000: {}%".format(greater_percent))
