import pandas as pd

file = pd.read_csv("../../datasets/Wine.csv")

print(file.columns)
print(file.values)