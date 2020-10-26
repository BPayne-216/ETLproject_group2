import pandas as pd


# Read the csv file in
df2 = pd.read_csv('Database/Tables/RottenTomatoesTop10.csv')

# Save to file
df2.to_html('HTML_files/rotten_tomatos.html', index=False)

# Assign to string
table4 = df2.to_html()
print(table4)