import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.dates as mdates
import datetime

data = np.genfromtxt("ghi.csv",delimiter=",", skip_header=1 )
axis = []
#x = np.random(data.shape[0])

start = datetime.datetime(2022,5,23)
end = datetime.datetime(2022,5,24)
curr = start
while(curr < end):
    axis.append(curr)
    curr = curr + datetime.timedelta(minutes=1)
    
print(len(axis))

#plt.xticks(axis, data[:1440,0])
plt.title("GHI Trend for 05/23/2022")
#print(axis.shape,data[:,1].shape)
plt.ylabel("GHI (W/m2)")
plt.xlabel("Time (mins)")
print(data[:,2],data[:,2].shape)
l1 = plt.scatter(axis, data[0:1441,1])
l2 = plt.scatter(axis, data[0:1441,2])
plt.legend(handles=[l1, l2], labels=['GHI from AlsoEnergy ', 'GHI from SunnyPortal'], loc='best')


plt.show()
