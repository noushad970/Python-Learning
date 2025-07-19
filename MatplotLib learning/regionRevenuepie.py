import matplotlib.pyplot as plt
region=['East','West','North','South']
revenue=[1000,2000,4000,2300]
plt.pie(revenue,labels=region,autopct='%1.1f%%')
plt.legend()
plt.title('Revenue by every region')
plt.show()