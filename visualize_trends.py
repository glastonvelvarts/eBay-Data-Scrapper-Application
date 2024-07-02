import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel('ebay_products.xlsx')

# Convert Price to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop rows with missing values
df.dropna(subset=['Price'], inplace=True)

# Plot price trends
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
