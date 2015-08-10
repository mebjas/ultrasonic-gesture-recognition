import serial
import numpy as np
from matplotlib import pyplot as plt

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
 
plt.ion() # set plot to animated
 
ydata = [0] * 100
ax1 = plt.axes()  
 
# make plot
line, = plt.plot(ydata)
plt.ylim([0,200])
plt.xlim([0,100])
# show plot
plt.show()

# start data collection
while True:  
    data = ser.readline().rstrip() # read data from serial 
                                   # port and strip line endings

    print data

    ydata.append(float(data))
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata)  # update the data
    plt.draw() # update the plot

 # clean up
analogPlot.close()