import matplotlib.pyplot as plt

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, 'r-.s')
listx2 = [2,8,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, 'k:s')
listx3 = [2,3,3,12,13,15]
listy3 = [10,50,40,40,40,60]
plt.plot(listx3, listy3, 'g--s')
plt.show()