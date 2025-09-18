import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
sns.load_dataset("titanic")
df = sns.load_dataset("titanic")
sns.scatterplot(data=df, x="age", y="fare", hue="class")