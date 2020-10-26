import pandas as pd

# Read the csv file in
df1 = pd.read_csv('Database/Tables/RottenTomatoes-Action.csv')

# Save to file
df1.to_html('HTML_files/rotten_tomatos.html', index=False)

# Assign to string
table3 = df1.to_html()
print(table3)