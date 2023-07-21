from matplotlib import pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-dark')

ages_x = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38,]
x_indexes = np.arange(len(ages_x))
width = 0.25

salary_y = [2000, 30000, 400, 50000, 5000, 6000, 60, 8000, 1200, 14000,]
plt.bar(x_indexes - width, salary_y, width=width, label="Ages",)

salary_B = [2005, 3000, 4000, 500, 500, 600, 600, 800, 120, 1400,]
plt.bar(x_indexes, salary_B, width=width, label="Salary B")

salary_c = [5000, 50, 6000, 20000, 90000, 1000, 800, 600, 30000, 2000]
plt.bar(x_indexes + width, salary_c, width=width, label="Salary C")

plt.title("Salary (USD)by tha Age")
plt.xlabel("Ages")
plt.ylabel("Salaries in (USD)")

plt.legend()

plt.show()