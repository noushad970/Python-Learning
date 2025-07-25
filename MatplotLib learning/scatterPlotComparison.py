import matplotlib.pyplot as plt
hourStudy=[1,2,3,4,5,6,7,8]
examScores1=[50,55,60,65,70,75,80,85]
examScores2=[52,56,61,69,73,78,84,89]

plt.scatter(hourStudy,examScores1,color='purple',marker='o',label='Student 1 Data')
plt.scatter(hourStudy,examScores2,color='green',marker='o',label='Student 2 Data')
plt.title('Comparision between 2 students')
plt.xlabel('Hours Studied',color='blue')
plt.ylabel('Obtained Mark',color='green')
plt.legend()
plt.grid(True)
plt.savefig('StudenComparison.png',dpi=300,bbox_inches='tight')
plt.show()