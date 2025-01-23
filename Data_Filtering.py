import pandas as pd

# Load your data into a DataFrame (assuming it's in a CSV file)
df = pd.read_csv('Angle_Distance.csv')  # Adjust separator if necessary

# Group by 'Class' and 'Sequence' and take the first 76 rows of each group
filtered_df = df.groupby(['Class', 'Sequence']).head(76)

# Save the result if needed
filtered_df.to_csv('First76.csv', index=False)

# Print a preview
print(filtered_df)
