import pandas as pd

india_weather = pd.DataFrame({                          # keys are the columns 
        "city": ["mumbai", "delhi", "bangalore"],
        "temperature": [32,45,30],
        "humidity": [80,60,78]
})
print(india_weather)

us_weather = pd.DataFrame({
        "city": ["new york", "chicago", "orlando"],
        "temperature": [21,14,35],
        "humidity": [68,65,75]
})
print(us_weather)

df = pd.concat([india_weather, us_weather]) # This will keep the original index
print(df)

df = pd.concat([india_weather, us_weather], ignore_index=True) # this will create a new index sequel 
print(df)

df = pd.concat([india_weather, us_weather], keys=["india", "us"]) # this will create keys 
print(df)

print(df.loc["india"]) # thats like a hashmap 

temperature_df = pd.DataFrame({
        "city": ["mumbai","delhi","banglore"],
        "temperature": [32,45,30]
}, index = [0,1,2])                             # with inded you can specify the index order
print(temperature_df)

wind_df = pd.DataFrame({
        "city": ["delhi","mumbai"],
        "windspeed": [7,12]
}, index = [1,0])
print(temperature_df)

print(pd.concat([temperature_df,wind_df], axis=1)) # axis=1 is columns 

df1 = pd.DataFrame({
        "city": ["mew york", "chicago","orlando"],
        "temperature": [21,14,35]
})

df2 = pd.DataFrame({
        "city": ["mew york", "chicago","orlando"],
        "humidity": [65,68,75]
})

df3 = pd.merge(df1,df2, on="city") # by default this is inner join
print(df3)

df1 = pd.DataFrame({
        "city": ["new york","chicago","orlando","baltimore"],
        "temperature": [21,14,35,38]
})
df2 = pd.DataFrame({
        "city": ["chicago","new york","san diego"],
        "humidity": [65,68,71]
})
df3 = pd.merge(df1, df2, on="city", how="inner")
print(df3)
df3 = pd.merge(df1, df2, on="city", how="left")
print(df3)
df3 = pd.merge(df1, df2, on="city", how="outer")
print(df3)