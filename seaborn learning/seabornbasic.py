import seaborn as sns

import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("people")

# Create a simple scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

plt.title("Total Bill vs Tip")
plt.show()