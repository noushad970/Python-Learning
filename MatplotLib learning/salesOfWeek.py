import matplotlib.pyplot as plt
x=['Sun','Mon','Tues','Wed','Thus','Fri']
y=[6,8,65,32,2,4]
plt.plot(x,y,color="green",linestyle='--',linewidth='2',marker='o')
plt.title("Sales of the week")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend(loc='upper left')
plt.grid(color='gray',linewidth='0.1')
# plt.xticks([],[])
plt.show()