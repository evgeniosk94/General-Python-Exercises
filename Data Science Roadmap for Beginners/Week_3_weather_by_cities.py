import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

print(df[df.city=="new york"].temperature.max())

g = df.groupby("city") # object creation, You create 3 dataframes since we have 3 cities. You can ran for loop in this object
print(g)

for city, data in g:            # city index is city as we created the object based on city. data index is the actual dataframe
        print("city:",city)
        print("\n")
        print("data:",data)
        
for city, data in g:            # city index is city as we created the object based on city. data index is the actual dataframe
        print("city:",city)
        print("max temp:",data.temperature.max())
        print("\n")
        
print(g.get_group("paris")) # Because g is an object we can apply .get_group operation and print the dataframe for paris 
print(g.max())
print(g.mean(numeric_only=True))
print(g.describe())
