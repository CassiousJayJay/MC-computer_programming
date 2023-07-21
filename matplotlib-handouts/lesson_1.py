from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-dark')

ages_x = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38,]
salary_y = [2000, 30000, 400, 50000, 5000, 6000, 60, 8000, 1200, 14000,]

plt.plot(ages_x, salary_y, "k--", label="All ages", linewidth="3")

salary_B = [2005, 3000, 4000, 500, 500, 600, 600, 800, 120, 1400,]
plt.plot(ages_x, salary_B, "b", label="Salaries", linewidth="5")

plt.title("Salary (USD)by tha Age")
plt.xlabel("Ages")
plt.ylabel("Salaries in (USD)")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("plot.png")
plt.show()