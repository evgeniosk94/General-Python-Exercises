import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("canada_per_capita_income.csv")

plt.figure()
plt.ylabel("Income per capita (US$)")
plt.xlabel("Year")
plt.scatter(df.year, df["per capita income (US$)"])


reg = linear_model.LinearRegression()
X = df.year.values.reshape(-1,1)
y = df["per capita income (US$)"]
reg.fit(X,y)

print(f"The income per capita in Canada in 2020 will be: {round(float(reg.predict([[2020]])),2)} dollars")

plt.figure()
plt.ylabel("Income per capita (US$)")
plt.xlabel("Year")
plt.scatter(df.year, df["per capita income (US$)"], marker="+", color="red")
plt.plot(df.year, reg.predict(df[["year"]]))

plt.show()