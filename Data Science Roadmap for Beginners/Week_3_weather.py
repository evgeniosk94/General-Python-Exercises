import pandas as pd
import numpy as np

# def converter(value):
#         if value == "-99999" or value == "-88888":
#                 return np.nan
#         return float(value)

# df = pd.read_csv("weather_data.csv", parse_dates=["day"], converters = {    # parse_dates method will convert data type of day column to date and time type 
#        "temperature": converter,                                            # converter will apply a function to selected columns 
#        "windspeed": converter}
#                  ) 

df = pd.read_csv("weather_data.csv", parse_dates=["day"])
print(df)

print(type(df.day[0]))
print(type(df.temperature[0]))
print(type(df.windspeed[0]))

df.set_index("day", inplace=True)
print(df)

df.fillna(0) # It need inplace=True 
print(df)

# df.fillna(method="ffill", inplace=True) # forward fill will put the previous value to a NaN value, there is also bakward fill bfill, limit=1 will put value to only 1 NaN in a row
# print(df)

print(df.interpolate(inplace=True)) # this will fill the NaN values with the interpolation method 

# df.fillna({                                     # you can pass a dictionary inside the fillna method, where the keys will be column names 
#         'temperature': df.temperature.mean(),
#         'windspeed': df.windspeed.mean(),
#         'event': 'No Event'
# }, inplace=True)

# dropna(how="all") will all will drop only the rows at which all columns have NaN values, how="any" will drop any row that has at least one NaN value 

print(df)