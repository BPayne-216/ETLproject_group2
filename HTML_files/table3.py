import pandas as pd

# Read the csv file in
df = pd.read_csv('Database/Tables/RottenTomatoes-1970.csv')

# Save to file
df.to_html('HTML_files/rotten_tomatos.html', index=False)

# Assign to string
table2 = df.to_html()
print(table2)