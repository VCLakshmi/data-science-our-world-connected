import pandas as pd
import matplotlib.pyplot as plt


internet_users = pd.read_csv("data/raw/extension-internet-users-by-continent.csv")
world_population_by_continent = pd.read_csv("data/raw/extension-historical-population-by-continent.csv")

# Merge both world population and internet users
internet_users_and_population = internet_users.merge(world_population_by_continent, on=["year", "continent"], how="left")

# determine the percentage of internet users in each year in each continent.
internet_users_and_population["percent"] = internet_users_and_population.eval("internet_users/population * 100")

# save to a file.
internet_users_and_population.to_csv("data/processed/internet-population-by-continent.csv", index=False)
print("\nInternet users and the population by continent")
print(internet_users_and_population)

# determine the year when more than 50% of the population in Asia got access to internet.
df = internet_users_and_population.query("continent == 'Asia' and percent >= 50")
more_than_50_percent_users = df.head(1)
more_than_50_percent_users = more_than_50_percent_users["year"].values
print(f"\nMore than 50% of the population in Asian Continent started using internet in the year: {more_than_50_percent_users}")
