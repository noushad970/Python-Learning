import matplotlib.pyplot as plt
x=['Sun','Mon','Tues','Wed','Thus','Fri']
y=[6,8,65,32,2,4]
plt.bar(x,y,color="green",label='Sales on week 2')
plt.title("Sales of the week")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
# plt.xticks([],[])
plt.show()