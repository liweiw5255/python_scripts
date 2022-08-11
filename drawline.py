from concurrent.futures import thread
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats

threshold = 0.5

#data1 = np.loadtxt("data-part1_2022_07_22.csv",delimiter=",")
#data2 = np.loadtxt("data-part2.csv",delimiter=",")
#data = np.concatenate((data1, data2), axis=0)
data = np.loadtxt("20220809.csv",delimiter=",")

z = np.abs(stats.zscore(data))

sma_fig, sma_axs = plt.subplots(2,3)
#solectria_fig, solectria_axs = plt.subplot(6)

for i in range(1,7):
    x = int((i-1)/3)
    y = (i - x*3 - 1)%3
    #x = int((i-7)/3)
    #y = (i-6 - x*3-1)%3
    #plt.subplot(2,3,i)
    x_data = data[:,0]/(60*60)
    y_data = data[:,i]

    #x_data = np.delete(x_data, z[:,i]<threshold)
    #y_data = np.delete(y_data, z[:,i]<threshold)

    sma_axs[x, y].plot(x_data, y_data)
    #sma_axs[x,y].set_title("SMA Fan "+str(i))
    sma_axs[x,y].set_ylim((0,0.06))
    sma_axs[x,y].set_title("SMA Fan "+str(i))
    #plt.plot(data[:,0],data[:,i])
    #sma_axs[x, y].title())
    sma_axs[x, y].set(xlabel= 'Duration (H)', ylabel= 'Current (A)')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)


plt.show()


for i in range(7,13):
    x = int((i-7)/3)
    y = (i - x*3 - 7)%3
    #x = int((i-7)/3)
    #y = (i-6 - x*3-1)%3
    #plt.subplot(2,3,i)
    x_data = data[:,0]/(60*60)
    y_data = data[:,i]

    #x_data = np.delete(x_data, z[:,i]<threshold)
    #y_data = np.delete(y_data, z[:,i]<threshold)

    sma_axs[x, y].plot(x_data, y_data)
    #sma_axs[x,y].set_title("SMA Fan "+str(i))
    sma_axs[x,y].set_ylim((0,0.64))
    sma_axs[x,y].set_title("NMB Fan "+str(i-6))
    #plt.plot(data[:,0],data[:,i])
    #sma_axs[x, y].title())
    sma_axs[x, y].set(xlabel= 'Duration (H)', ylabel= 'Current (A)')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()

