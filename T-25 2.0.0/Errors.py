

##Errors below
##100: Op mode not avaible
##101: Op mode Unkown
##200: E-STOP Engaged
##300: Unknown Command
##400: Hard reset requird to return to operations
##500: Car Error
##510: G-Force High Error
##520: G-Force Low Error
##530: Lateral G-Force Error
##540: Speed Error
##550: Rider Weight Outside SOP
##560: Car Gyro Error
##570: Car Brake Error

from ridemusic import errorsound
from estop import shortclock
import datetime
import os
os.chdir('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs')



def E100():
    errorsound()
    print("Error 100: Op mode not available")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 100:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E101():
    errorsound()
    print("Error 101: Op mode Unkown")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 101:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E200():
    errorsound()
    print("Error 200: E-Stop Engaged")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 200:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E300():
    errorsound()
    print("Error 300: Unkown Command")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 300:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E400():
    errorsound()
    print("Error 400: Hard Reset Required to return to Operations")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 400:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E500():
    errorsound()
    print("Error 500: Car Error")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 500:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E510():
    errorsound()
    print("Error 510: G-Force High Error ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 510:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E520():
    errorsound()
    print("Error 520: G-Force Low Error")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 520:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E530():
    errorsound()
    print("Error 530: Lateral G-Force Error ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 530:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E540():
    errorsound()
    print("Error 540: Speed Error ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 540:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E550():
    errorsound()
    print("Error 550: Rider Weight Outside SOP ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 550:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E560():
    errorsound()
    print("Error 560: Car Gyro Error ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 560:" + str(current_date) + "\n")
    fh.close()
    shortclock()
def E570():
    errorsound()
    print("Error 570: Car Brake Error ")
    fh = open('errorLogs.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("\n" + "Error 570:" + str(current_date) + "\n")
    fh.close()
    shortclock()
