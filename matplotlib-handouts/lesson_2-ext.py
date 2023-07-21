from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

plt.style.use('seaborn-v0_8-dark')

data = pd.csv_reader("entrprise_survey.csv")
ids = data["Year"]



# using conunter
# with open("entrprise_survey.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

language_counter = Counter()

for row in csv_reader:
    language_counter.update(row["Year"].split(";"))
languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

plt.bar(languages, popularity)
plt.title("Most popular year")
plt.xlabel("Year")
# plt.ylabel("Common language")
plt.tight_layout()
plt.show()