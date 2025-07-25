import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def loadData(s):
    return "C:/Users/user/Desktop/Python-Learning/seaborn learning/"+s

# print(sns.get_dataset_names())

# print("Dataset loaded successfully")

# print("Name: "+data['First Name'].head()+" "+ data['Last Name'].head()+" . Phone:"+ data['Phone'].head())

# sns.scatterplot(data=data, x="Total Bill", y="Tip")
df=sns.load_dataset("titanic")
# print(df.head())
sns.scatterplot( x="age", y="fare",data=df)
plt.title("Age vs Fare")
