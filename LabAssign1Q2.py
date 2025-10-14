import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---Graph 1:DJIA Open and Close Prices

dates = pd.date_range(start="2022-01-01", end="2023-01-01", freq="M")
open_prices = np.random.randint(29000, 37000, len(dates))
close_prices = open_prices + np.random.randint(-500, 500, len(dates))

plt.subplot(1, 2, 1) 
plt.plot(dates, open_prices, label="Open", color="blue")
plt.plot(dates, close_prices, label="Close", color="orange")
plt.title("DJIA Open and Close Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
# ---Graph 2:Students Passed
years = [2015, 2016, 2017, 2018, 2019]
IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 30, 23, 25, 17]

x = np.arange(len(years)) 
width = 0.26  
plt.subplot(1, 2, 2)  
plt.bar(x - width, IT, width, label="IT", color="red")
plt.bar(x, ECE, width, label="ECE", color="green")
plt.bar(x + width, CSE, width, label="CSE", color="blue")

plt.xlabel("Branch", fontweight="bold")
plt.ylabel("Students passed", fontweight="bold")
plt.xticks(x, years)
plt.legend()

plt.tight_layout()
plt.show()
