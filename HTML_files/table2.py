import pandas as pd

# Read the csv file in
df = pd.read_csv('Database/Tables/RottenTomatoes-13+.csv')

# Save to file
df.to_html('HTML_files/rotten_tomatos.html', index=False)

# Assign to string
table = df.to_html()
print(table)
