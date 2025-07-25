import matplotlib.pyplot as plt
hourStudy=[1,2,3,4,5,6,7,8]
examScore=[50,55,60,65,70,75,80,85]
plt.scatter(hourStudy,examScore,color='purple',marker='o',label='Student Data')
plt.xlabel('Hours Studied')
plt.ylabel('Obtained Mark')
plt.legend()
plt.grid(True)
plt.show()