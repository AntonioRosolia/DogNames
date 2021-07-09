import pandas as pd
from textdistance import levenshtein

reference_name = "Luca"
df = pd.read_csv("20210103_hundenamen.csv")

df["LD"]=df.apply(lambda x: levenshtein.distance(x['HUNDENAME'],  reference_name), axis=1)
result = df[df["LD"]==1]["HUNDENAME"].unique()