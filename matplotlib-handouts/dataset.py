from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

plt.style.use('seaborn-v0_8-dark')

data = pd.csv_reader("entrprise_survey.csv")
years = data["Year"]
industry = data["Industry_aggregation_NZSIO"]

for year in years:
    pass