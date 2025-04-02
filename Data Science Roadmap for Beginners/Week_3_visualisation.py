import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df_sales = pd.read_excel("linechart.xlsx")
print(df_sales.head())

plt.figure(figsize=(12,4))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="green", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="orange", label="Washing Machine")

plt.title("Product sales")
plt.xlabel("Financial Quarter")
plt.ylabel("Revenue (mln $)")
plt.legend()


total_sales = df_sales[["Fridge", "Dishwasher", "Washing Machine"]].sum()
plt.figure()
plt.pie(total_sales, labels=total_sales.index, autopct="%1.2f%%", explode=(0.1,0,0), shadow=True, startangle=140)

df_sales.plot(kind="bar", x="Quarter")
plt.xticks(rotation=45)

df_sales_2 = df_sales.set_index("Quarter")

df_sales_2.plot(kind="bar")
plt.xticks(rotation=45)

plt.figure()
df_score = pd.read_excel("histograms.xlsx")
plt.hist(df_score["Exam_Score"])

plt.figure()
sns.histplot(data=df_score, x="Exam_Score", kde=True)

df = pd.read_excel("scatter_plot.xlsx")
plt.figure()
sns.scatterplot(data=df, x="area_square_ft", y="price")

plt.show()