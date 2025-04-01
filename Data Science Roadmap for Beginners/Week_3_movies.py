import csv
import pandas as pd


# Python way
def calculate_ratings_stats(data, industry=None):
        ratings = []
        for row in data:
                if row[3]!="NULL" and (not industry or row[1]==industry):
                        ratings.append(float(row[3]))
        max_rating = max(ratings)
        min_rating = min(ratings)
        avg_rating = sum(ratings)/len(ratings)
        return max_rating, min_rating, avg_rating                

with open("movies.csv") as f:
        data = list(csv.reader(f))
        header = data[0]
        data = data[1:]
        
max_rating, min_rating, avg_rating = calculate_ratings_stats(data)
print(f"All records: Min rating = {min_rating}, Max rating =  {max_rating}, Avg rating = {avg_rating}")


max_rating, min_rating, avg_rating = calculate_ratings_stats(data, industry="Bollywood")
print(f"Bollywood: Min rating = {min_rating}, Max rating =  {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_ratings_stats(data, industry="Hollywood")
print(f"Hollywood: Min rating = {min_rating}, Max rating =  {max_rating}, Avg rating = {avg_rating}")


# Pandas way
df = pd.read_csv("movies.csv")
print(df.sample(5)) # instead of head/tail, sample returns random rows of the dataframe 
#print(df.imdb_rating)
print(type(df)) # type 
print(type(df.imdb_rating)) # type of a column is a dataframe is series 
#print(dir(df.imdb_rating))  # dir returns the list of functions you can apply to series 

print(df.imdb_rating.min(), df.imdb_rating.max(), df.imdb_rating.mean())
print(df[df.industry=="Bollywood"].imdb_rating.min(), df[df.industry=="Bollywood"].imdb_rating.max(), df[df.industry=="Bollywood"].imdb_rating.mean())
print(df[df.industry=="Hollywood"].imdb_rating.min(), df[df.industry=="Hollywood"].imdb_rating.max(), df[df.industry=="Hollywood"].imdb_rating.mean())

print(df.columns)
print(df.industry.unique())
print(df["language"].unique())
print(df.industry.value_counts())
print(df.language.value_counts())

df_new = df[["title","imdb_rating","industry"]]
print(df_new)
print(df[(df.release_year>=2000) & (df.release_year<=2010)])

print(df.describe())

df["age"] = df["release_year"].apply(lambda x: 2025 - x) # on release_year column I will apply some kind of transformation, lambda x a quickly way of writing a python function, sort of for loop for each row for release_year column
print(df.head())

#df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1) # this is when applying a transforamtion using two columns of the dataframe
df["profit"] = df["revenue"] - df["budget"]

print(df.head())

df.set_index("title", inplace=True)
print(df.head())

# print(df.loc[["Pather Panchali", "Avatar"]]) # loc is location on labaled based index 

print(df.iloc[0:2]) # iloc is integer based index location

df.reset_index(inplace=True)
