from concurrent.futures import thread
from datetime import date
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats

#data1 = np.loadtxt("data-part1_2022_07_22.csv",delimiter=",")
#data2 = np.loadtxt("data-part2.csv",delimiter=",")
#data = np.concatenate((data1, data2), axis=0)


def draw_sma(data, dt):

    sma_fig, sma_axs = plt.subplots(2,3)

    for i in range(1,7):
        x = int((i-1)/3)
        y = (i - x*3 - 1)%3
        x_data = data[:,0]/(60*60)
        y_data = data[:,i]

        sma_axs[x, y].plot(x_data, y_data)
        sma_axs[x,y].set_ylim((0,0.06))
        sma_axs[x,y].set_title("SMA Fan "+str(i))
        sma_axs[x, y].set(xlabel= 'Duration (H)', ylabel= 'Current (A)')

    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)


    plt.show()
    #plt.savefig("plots/sma_"+dt+".png")

def draw_solectria(data, dt):

    solectria_fig, solectria_axs = plt.subplots(2,3)

    for i in range(7,13):
        x = int((i-7)/3)
        y = (i - x*3 - 7)%3
        
        x_data = data[:,0]/(60*60)
        y_data = data[:,i]

        solectria_axs[x,y].plot(x_data, y_data) 
        solectria_axs[x,y].set_ylim((0,0.7))
        solectria_axs[x,y].set_title("NMB Fan "+str(i-6))
        solectria_axs[x,y].set(xlabel= 'Duration (H)', ylabel= 'Current (A)')

    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)

    plt.show()
    #plt.savefig("plots/nmb_"+dt+".png")


def main():
    
    dt = input("Please input date: ")

    data = np.loadtxt("fan_data/"+dt+".csv",delimiter=",")

    draw_sma(data,dt)

    draw_solectria(data,dt)


if __name__ == "__main__":
    main()