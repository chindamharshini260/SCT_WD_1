import pandas as pd
import matplotlib.pyplot as plt

# Skip the first 4 metadata rows
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_346039/API_SP.POP.TOTL_DS2_en_csv_v2_346039.csv",
    skiprows=4
)

# Take top 10 countries by population in 2023
top10 = df[['Country Name', '2023']].dropna()
top10 = top10.sort_values(by='2023', ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(top10['Country Name'], top10['2023'])

plt.title('Top 10 Countries by Population (2023)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()