import requests
import pandas as pd
import matplotlib.pyplot as plt

from io import StringIO


# headers
headers = {"User-Agent": "Mozilla/5.0"}

# Internet users dataset
internet_url = "https://ourworldindata.org/grapher/share-of-individuals-using-the-internet.csv"

# download the internet users dataset
response = requests.get(internet_url, headers=headers)
response.raise_for_status()  # will raise error if still blocked

# read csv and save it to the processed data.
internet_users = pd.read_csv(StringIO(response.text))
internet_users.to_csv("data/processed/internet-users-by-region.csv", index=False)

print("\nShare of Internet users across different regions:")
print(internet_users)


# Population dataset
population_url = "https://ourworldindata.org/grapher/population.csv"

# download the population dataset
response = requests.get(population_url, headers=headers)
response.raise_for_status()

# read csv and save it to the processed data.
population = pd.read_csv(StringIO(response.text))
population.to_csv("data/processed/population-by-region.csv", index=False)

print("\nPopulation data across different regions:")
print(population)


internet_users_and_population = internet_users.merge(
                                    population,
                                    on=["Year", "Entity", "Code"],
                                    how="left"
                                )
print("\nCombined data frame showing population across different regions and the percent of internet users:")
print(internet_users_and_population)


## compute the dataframe for the population and the percentage of internet users in India over the years
df_india = internet_users_and_population.query("Entity == 'India'").dropna()

print("\nPopulation and Percentage of Internet users in India over the years:")
print(df_india)

# plot the graph
plt.plot(df_india["Year"], df_india["Share of the population using the Internet"], label="Internet Users (%)")
plt.legend()
plt.axhline(50, color="gray", linestyle="dotted")

# Add xlabel, ylabel, and title
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.title("Percentage of Internet users in India over the years")

# Save the graph
plt.savefig("outputs/figures/percentage_of_internet_users_in_india.png")
plt.show()