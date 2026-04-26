import pandas as pd
import matplotlib.pyplot as plt


# read world population data
population = pd.read_csv("data/raw/historical-world-population.csv")
# read internet users data
internet_users = pd.read_csv("data/raw/world-internet-users.csv")


# Create a new data frame that shows the internet users from the total world population on the particular year.
internet_users_world_population = internet_users.merge(population, on="year", how="left")

# strip off the frames where the internet users are NaN
internet_users_world_population = internet_users_world_population.dropna()
print("\nData frame shows the number of internet users against among the total population against the given year")
print(internet_users_world_population)

# percentage of the world connected to internet each year
internet_users_world_population["percent"] = internet_users_world_population.eval("internet_users/population * 100")
internet_users_world_population["percent"] = internet_users_world_population["percent"].round(2)
print("\nNew data frame where percent of internet users added for each year.")
print(internet_users_world_population)


## Plot the percentage of internet users over the time.
plt.plot(internet_users_world_population["year"], internet_users_world_population["percent"])
plt.axhline(50, color="gray", linestyle="--")
plt.xlabel("year")
plt.ylabel("percentage of internet users")
plt.title("Percentage of Internet Users over time")

# save the figure
plt.savefig("outputs/figures/percentage_of_internet_users.png")
plt.show()


# Find the year where the internet users crossed 50% of world population
df = internet_users_world_population.query("percent >= 50")
year = df.head(1)
print(f"\nYear where the internet users crossed 50% of world population for the first time: {year["year"].values}")