import pandas as pd


# Read the csv file in
df = pd.read_csv('Database/Tables/RottenTomatoes-Western.csv')

# Save to file
df.to_html('HTML_files/table.html', index=False)

# Assign to string
table = df.to_html()
print(table)

