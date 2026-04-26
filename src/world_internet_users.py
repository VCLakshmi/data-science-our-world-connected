import pandas as pd
import matplotlib.pyplot as plt

internet_users = pd.read_csv("data/raw/world-internet-users.csv")
print(internet_users)

# find the year where the internet users exceeded 100 million
users_100_million = internet_users.query("internet_users > 100000000")
# first year where the internet users has crossed 100 million
users_100_million = users_100_million.head(1)
year = users_100_million["year"].values
print(f"\nYear where the internet users crossed 100 million users for the first time: {year}")

