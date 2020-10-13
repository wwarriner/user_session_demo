import pandas as pd

# Create some artificial data
data = [{"A": 1, "B": 2, "C": 3}, {"A": 4, "B": 5, "C": 6}]
df = pd.DataFrame(data)
# ! Debug
print(df.to_string())

# HACK hardcoding names for now
# TODO better name
df.to_csv("env_test.csv")

xlsx_writer = pd.ExcelWriter("env_test.xlsx", engine="xlsxwriter")
df.to_excel(xlsx_writer)
xlsx_writer.save()
# ? Any other output formats needed
